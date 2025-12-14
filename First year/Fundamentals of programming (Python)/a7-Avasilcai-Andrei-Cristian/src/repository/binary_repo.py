import pickle

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

class BinaryRepository:
    def __init__(self, file_path):
        self._file_path = file_path
        self._history = []
        self._data = {}
        self._load_data()

    def save_state(self):
        """Save the current state of the repository."""
        self._history.append(self._data.copy())
        self._save_data()

    def _load_data(self):
        """Load books from the binary file."""
        try:
            with open(self._file_path, "rb") as file:
                self._data = pickle.load(file)
        except FileNotFoundError:
            print(f"File {self._file_path} not found. Starting with empty repository.")
        except Exception as e:
            print(f"Error loading binary file {self._file_path}: {e}")

    def _save_data(self):
        """Save the books to the binary file."""
        try:
            with open(self._file_path, "wb") as file:
                pickle.dump(self._data, file)
        except Exception as e:
            print(f"Error saving data to {self._file_path}: {e}")

    def add(self, book):
        """Add a new book to the repository if the ISBN is unique."""
        self.save_state()
        if book.isbn in self._data:
            raise DuplicateISBNError(f"A book with ISBN {book.isbn} already exists.")
        self._data[book.isbn] = book
        self._save_data()

    def remove(self, isbn: str):
        """Remove a book by its ISBN."""
        self.save_state()
        if isbn not in self._data:
            raise ISBNNotFoundError(f"Book with ISBN {isbn} not found in the repository.")
        removed_book = self._data.pop(isbn)
        self._save_data()
        return removed_book

    def get_all(self):
        """Return a list of all books in the repository."""
        return list(self._data.values())

    def undo(self):
        """Undo the last modification."""
        if not self._history:
            raise IndexError("No operations to undo.")
        self._data = self._history.pop()
        self._save_data()
        print("Undo successful")

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
