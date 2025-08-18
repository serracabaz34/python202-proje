from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests


app = FastAPI()

# data models 

class Book(BaseModel):
    isbn: str
    title: str
    author: list[str]

class ISBNRequest(BaseModel):
    isbn: str

library = {}   # isbn -> Book

def fetch_book_from_openlibrary(isbn: str):
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    title = data.get("title", "Unknown Title")
    authors = []

    if "authors" in data:
        for author in data["authors"]:
            author_data = requests.get(f"https://openlibrary.org{author['key']}.json").json()
            authors.append(author_data.get("name", "Unknown Author"))

    return Book(isbn=isbn, title=title, authors=authors)

# GET /books
@app.get("/books")
def get_books():
    return list(library.values())

# POST /books
@app.post("/books")
def add_book(isbn_request : ISBNRequest):
    isbn = isbn_request.isbn
    if isbn in library:
        raise HTTPException(status_code=400, detail="Book already exists")

    book = fetch_book_from_openlibrary(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Book Not Founded")

    library[isbn] = book
    return book

# DELETE /books/{isbn}
@app.delete("/books/{isbn}")
def delete_book(isbn : str):
    if isbn not in library:
        raise HTTPException(status_code=404, detail="Book Not Founded")
    deleted = library.pop(isbn)
    return deleted
    