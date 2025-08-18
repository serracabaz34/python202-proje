import os
import json
import pytest
from book import Book
from library import Library

TEST_FILE = "library.json"

@pytest.fixture
def temp_library():
    """temporary test library"""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    lib = Library(TEST_FILE)
    yield lib
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_book(temp_library):
    book = Book("Test Kitap", "Test Yazar", "12345")
    assert temp_library.add_book(book) == True
    assert len(temp_library.books) == 1

def test_remove_book(temp_library):
    book = Book("Test Kitap", "Test Yazar", "12345")
    temp_library.add_book(book)
    assert temp_library.remove_book("12345") == True
    assert len(temp_library.books) == 0

def test_find_book(temp_library):
    book = Book("Test Kitap", "Test Yazar", "12345")
    temp_library.add_book(book)
    found = temp_library.find_book("12345")
    assert found is not None
    assert found.title == "Test Kitap"

def test_list_books(temp_library):
    temp_library.add_book(Book("Kitap 1", "Yazar 1", "111"))
    temp_library.add_book(Book("Kitap 2", "Yazar 2", "222"))
    assert len(temp_library.books) == 2