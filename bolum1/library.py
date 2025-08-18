import json
import os
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """Load the books from the JSON file"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                try:
                   data = json.load(f)
                   self.books = [Book(**book) for book in data]
                except json.JSONDecodeError:
                   self.books = []
        else:
           self.books = []

    def save_books(self):
        """save the books to json"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([book.__dict__ for book in self.books], f,ensure_ascii = False, indent=4)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def add_book(self, book):
        """Add new book"""
        if self.find_book(book.isbn):
            print("This ISBN already exists")
            return False
        self.books.append(book)
        self.save_books()
        print("Book added successfully")
        return True

    def remove_book(self, isbn):
        """According to isbn, delete book"""
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            print("The book is deleted")
            return True
        print("The book not found")
        return False

    def list_books(self):
        """List all the books"""
        if not self.books:
            print("Library is empty")
        for book in self.books:
            print(book)

