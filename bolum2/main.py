from library import Library

def main():
    lib = Library()

    while True:

        print("\n=== Library ===")
        print("1. Add Book (ISBN)")
        print("2. Delete Book (ISBN)")
        print("3. List Of Books")
        print("4. Search for books (ISBN)")
        print("5. Quit")

        secim = input("Your Choice: ").strip()

        if secim == "1":
            isbn = input("ISBN: ").strip()
            ok = lib.add_book(isbn)
            if ok:
                print("Added.")

        elif secim == "2":
            isbn = input("ISBN: ").strip()
            if lib.remove_book(isbn):
                print("Deleted.")
            else:
                print("Not Founded.")

        elif secim == "3":
            lib.list_books()

        elif secim == "4":
            isbn = input("ISBN: ").strip()
            b = lib.find_book(isbn)
            print("Founded:", b) if b else  ("Not Founded.")

        elif secim == "5":
            print("See You!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()