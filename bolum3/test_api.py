from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_add_and_get_books():
    response = client.post("/books", json = {"isbn": "9780140328721"})
    assert response.status_code == 200
    data = response.json()
    assert "title" in data

    get_response = client.get("/books")
    assert get_response.status_code == 200
    books = response.json()
    assert any(book["isbn"] == "9780140328721" for book in books)

def test_delete_book():
    isbn = "9780140328721"
    client.post("/books", json = {"isbn" : isbn})
    delete_response = client.delete(f"/books/{isbn}")
    assert delete_response.status_code == 200