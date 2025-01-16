# library_management.py

class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Represents a library managing a collection of books."""

    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only instances of the Book class can be added.")

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}' successfully.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}' successfully.")
                    return
                else:
                    print(f"'{title}' is already available.")
                    return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
