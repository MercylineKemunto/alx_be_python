class Book:
    """A class to represent a book."""

    def __init__(self, title, author, year):
        """Initialize a book with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to handle book deletion."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
