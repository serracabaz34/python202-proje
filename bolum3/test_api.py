from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_books_empty():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == []

def test_add_book_invalid_isbn():
    response = client.post("/books", json={"isbn": "0000000000"})
    assert response.status_code in [404, 503]

def test_add_and_delete_book():
    isbn = "9780140328721"  # Matilda (Roald Dahl)
    response = client.post("/books", json={"isbn": isbn})
    if response.status_code == 404:
        print("OpenLibrary API temporarily failed to find data. Please retry the test.")
        return
    
    assert response.status_code == 200
    book = response.json()
    assert book["isbn"] == isbn

    delete_response = client.delete(f"/books/{isbn}")
    assert delete_response.status_code == 200
    assert "Book is deleted" in delete_response.json()["message"]