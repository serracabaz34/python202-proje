import json
import os
import re
import httpx
from book import Book

OPENLIB_BASE = "https://openlibrary.org"

class Library:
    def __init__(self, filename="library.json", client: httpx.Client | None = None):
        self.filename = filename
        self.books = []
        # Testlerde taklit edebilmek için client enjekte edilebilir
        self.client = client or httpx.Client(timeout=10.0, base_url = OPENLIB_BASE)
        self.load_books()

    # Remove dashes/spaces in ISBN 
    def _normalize_isbn(self, isbn: str) -> str:
        return re.sub(r"[^0-9Xx]", "", isbn)
    
    def _fetch_book_from_openlibrary(self, raw_isbn: str) -> tuple[str, str, str]:
        """Get title + author names from Open Library (edition)."""
        isbn = self._normalize_isbn(raw_isbn)

        r = self.client.get(f"{OPENLIB_BASE}/isbn/{isbn}.json")
        if r.status_code == 404:
            raise LookupError("Book Not Founed (404).")
        r.raise_for_status()
        data = r.json()

        title = data.get("title")
        if not title:
            raise ValueError("'title' is missing from API response.")

        # authors: [{"key": "/authors/OL...A"}]
        author_names = []
        for a in data.get("authors", []): 
            key = a.get("key")  #example: "/authors/OL456789A"
            if not key:
                continue
            ar = self.client.get(f"{OPENLIB_BASE}{key}.json")
            if ar.status_code == 200:
                name = ar.json().get("name")
                if name:
                    author_names.append(name)

        author = ", ".join(author_names) if author_names else "Unknown"
        return title, author, isbn
    
    """UPDATED API: Gets ISBN"""
    def add_book(self, isbn: str) -> bool:
        norm = self._normalize_isbn(isbn)
        if self.find_book(norm):
            print("This isbn is available!")
            return False

        try:
            title, author, norm = self._fetch_book_from_openlibrary(isbn)
        except httpx.RequestError:
            print("Network error: Check your internet connection.")
            return False
        except LookupError:
            print("Book Not Founded.")
            return False
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return False

        self.books.append(Book(title, author, norm))
        self.save_books()
        return True
    
    def remove_book(self, isbn: str) -> bool:
        norm = self._normalize_isbn(isbn)
        before = len(self.books)
        self.books = [b for b in self.books if b.isbn != norm]
        changed = len(self.books) != before
        if changed:
            self.save_books()
            print("✅ Book is deleted!")
        return changed
    
    def list_books(self):
        if not self.books:
            print("Library is empty.")
            return
        for b in self.books:
            print(f"{b.title} - {b.author} - ISBN: {b.isbn}")

    def find_book(self, isbn: str):
        norm = self._normalize_isbn(isbn)
        for b in self.books:
            if b.isbn == norm:
                return b
        return None
    
    def load_books(self) -> None:
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.books = [Book(**item) for item in data]
            except json.JSONDecodeError:
                self.books = []
        else:
            self.books = []

    def save_books(self) -> None:
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([b.__dict__ for b in self.books], f, ensure_ascii=False, indent=2)