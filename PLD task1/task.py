from datetime import datetime

class BorrowedBook:
    def __init__(self, title, author, isbn, borrower_name=None, borrow_date=None, return_date=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrower_name = borrower_name
        self.borrow_date = borrow_date
        self.return_date = return_date

    def borrow(self, borrower_name):
        if self.borrower_name is None:
            self.borrower_name = borrower_name
            self.borrow_date = datetime.now().strftime("%Y-%m-%d")
            self.return_date = None
            print(f"{self.title} has been borrowed by {self.borrower_name}.")
        else:
            print(f"{self.title} is already borrowed by {self.borrower_name}.")

    def return_book(self):
        if self.borrower_name is not None:
            self.borrower_name = None
            self.return_date = datetime.now().strftime("%Y-%m-%d")
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is not currently borrowed.")

    def __str__(self):
        status = "Borrowed" if self.borrower_name else "Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)



def main():
    library = Library()
    library = read_from_text(library)

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Library")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            with open('books.txt','a') as file:
                file.write(title+"|"+author+"|"+isbn)
            book = BorrowedBook(title, author, isbn)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == '2':
            title = input("Enter title of the book to borrow: ")
            book = next((book for book in library.books if book.title == title), None)
            if book:
                book.borrow(input("Enter your name: "))
            else:
                print("Book not found in the library.")

        elif choice == '3':
            title = input("Enter title of the book to return: ")
            book = next((book for book in library.books if book.title == title), None)
            if book:
                book.return_book()
            else:
                print("Book not found in the library.")

        elif choice == '4':
            print("\nLibrary Catalog:")
            library.display_books()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")




def read_from_text(library):
    with open("books.txt", "r") as file:
       for line in file:
         data = line.strip().split("|")
         if len(data) == 3:
            book = BorrowedBook(data[0], data[1], data[2])
         elif len(data) == 5:
            book = BorrowedBook(data[0], data[1], data[2], data[3], data[4])
         else:
            print(f"Invalid data format: {line}")
            continue
         library.add_book(book)

    return library


if __name__ == "__main__":
    main()