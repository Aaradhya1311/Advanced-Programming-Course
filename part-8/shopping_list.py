class Book:
    """A book with details."""

    def __init__(self, name: str, author: str, genre: str, year: int) -> None:
        """Initialize the book with name, author, genre, and year.

        Args:
            name (str): The name of the book.
            author (str): The author of the book.
            genre (str): The genre of the book.
            year (int): The year the book was published.

        """
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"{self.name} by {self.author}, Genre: {self.genre}, Year: {self.year}"


if __name__ == "__main__":
    # Example usage
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

    print(python)
    print(everest)
