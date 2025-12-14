class RepositoryError(Exception):
    """Base class for exceptions in the repository."""

    def __init__(self, message="A repository error occurred"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class DuplicateISBNError(RepositoryError):
    """Raised when attempting to add an element with a duplicate ISBN."""

    def __init__(self, message="Duplicate object ISBN found"):
        super().__init__(message)


class ISBNNotFoundError(RepositoryError):
    """Raised when an element with a specified ISBN is not found in the repository."""

    def __init__(self, message="The specified ISBN was not found in the repository"):
        super().__init__(message)


class RepositoryIterator:
    def __init__(self, data):
        self.__data = data
        self.__pos = -1

    def __next__(self):
        self.__pos += 1
        if self.__pos >= len(self.__data):
            raise StopIteration()
        return self.__data[self.__pos]


class MemoryRepository:
    def __init__(self):
        self._data = {}
        self.history = []

    def save_state(self):
        """Save the current state of the repository."""
        self.history.append(self._data.copy())

    def add(self, book):
        """Add a new book if its ISBN is unique."""
        if book.isbn in self._data:
            raise DuplicateISBNError(
                f"A book with ISBN {book.isbn} already exists.")
        self.save_state()
        self._data[book.isbn] = book

    def remove(self, isbn: str):
        """Remove a book by its ISBN."""
        if isbn not in self._data:
            raise ISBNNotFoundError(
                f"Book with ISBN {isbn} not found in the repository.")
        self.save_state()
        removed_book = self._data.pop(isbn)

    def get_all(self):
        """Return a list of all books in the repository."""
        return list(self._data.values())

    def undo(self):
        """Undo the last modification."""
        if not self.history:
            raise IndexError("No operations to undo.")
        self._data = self.history.pop()
        print("Undo successful")

    def find(self, isbn: str):
        """Find a book by ISBN."""
        if isbn not in self._data:
            raise ISBNNotFoundError(
                f"Book with ISBN {isbn} not found in the repository.")
        return self._data[isbn]

    def __iter__(self):
        """Return an iterator for the books in the repository."""
        return RepositoryIterator(list(self._data.values()))

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]

    def __len__(self):
        """Return the number of books in the repository."""
        return len(self._data)
