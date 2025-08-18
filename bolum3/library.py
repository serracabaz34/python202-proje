from book import Book

class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_books(self):
        return self.books
    
    def delete_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False    