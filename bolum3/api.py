from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

from book import Book
from library import Library

app = FastAPI()
library = Library()

class ISBNRequest(BaseModel):
    isbn: str

# GET /books
@app.get("/books")
def get_books():
    return library.get_books()

# POST /books
@app.post("/books")
def add_book(isbn_request : ISBNRequest):
    isbn = isbn_request.isbn.replace("-", "")
    url = f"https://openlibrary.org/isbn/{isbn}.json"

    try:
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="OpenLibrary service could not be reached.")
    except httpx.HTTPStatusError:
        raise HTTPException(status_code=404, detail="Book Not Founded.")

    data = response.json()

    authors = []
    for a in data.get("authors", []):
        authors.append(a.get("name", "Unknown"))

    book = Book(
        title=data.get("title", "Unknown"),
        authors=authors,
        publish_date = data.get("publish_date"),
        isbn=isbn
    )

    library.add_book(book)
    return book

# DELETE /books/{isbn}
@app.delete("/books/{isbn}")
def delete_book(isbn : str):
    if library.delete_book(isbn):
        return {"message": f"Book is deleted : {isbn}"}
    raise HTTPException(status_code=404, detail="Book Not Founded")
    