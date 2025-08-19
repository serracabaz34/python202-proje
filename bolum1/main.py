from library import Library
from book import Book

def main():
    library = Library()

    while True:
        print("The Menu Of Library ")
        print("\n1. Add Book ")
        print("2. Delete Book ")
        print("3. List Book ")
        print("4. Find Book ")
        print("5. Quit ")

        choice = input("Your Choice: ")

        if choice == "1":
            title = input("Name Of The Book: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)

        elif choice == "2":
            isbn = input("ISBN to be deleted ")
            library.remove_book(isbn)
            print("Book is deleted")

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            isbn = input("ISBN to be called")
            book = library.find_book(isbn)
            if book:
                print("Book is founded:", book)
            else:
                print("Book not founded")

        elif choice == "5":
            print("It is quiting the programm...")
            break
        
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()