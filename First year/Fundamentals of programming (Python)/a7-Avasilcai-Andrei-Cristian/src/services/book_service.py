from src.domain.book import Book

class BookService:
    def __init__(self, repo):
        """
        The repo parameter is the repository passed from outside (e.g., MemoryRepository)
        :param repo: Repository-like object that implements the necessary methods
        """
        self._repo = repo

    def add_book(self, isbn: str, author: str, title: str):
        """
        Adds a book to the repository. Returns a success or error message.
        :param isbn: the unique identifier
        :param author: the author of the book
        :param title: the title of the book
        :return: success or error message
        """
        book = Book(isbn, author, title)
        try:
            self._repo.add(book)
            return "Book added successfully."
        except KeyError:
            return f"Error: Book with ISBN {isbn} already exists."
        except Exception as e:
            return f"Error: {str(e)}"

    def get_all(self) -> list:
        """
        Returns a list with all the books in the repository.
        :return: list of all books
        """
        return self._repo.get_all()

    def filter_books(self, word: str):
        """
        Remove books whose titles start with the given word.
        :param word: word to filter by
        :return: success message
        """
        self._repo.save_state()
        to_remove = [isbn for isbn, book in self._repo._data.items() if book.title.startswith(word)]
        for isbn in to_remove:
            return self._repo.remove(isbn)
        return f"Books with titles starting with '{word}' have been removed."

    def undo_action(self):
        """
        Undo the last operation.
        :return: success or failure message
        """
        try:
            self._repo.undo()
        except Exception as e:
            print(f"Cannot undo: {str(e)}")

