from src.domain.book import Book
from src.repository.memoery_repo import IDNotFoundError,  DuplicateIDError, TitleNotFoundError,AuthorNotFoundError


class IDValidatorException(KeyError):
    def __init__(self, message="A validation error occurred"):
        super().__init__(message)
        self.message = message

class ValidationException(Exception):
    def __init__(self, message = "A validation error occurred"):
        super().__init__(message)
        self.message = message

class BookService:
    def __init__(self, repo):
        """
        The repo parameter is the repository passed from outside (e.g., MemoryRepository)
        :param repo: Repository-like object that implements the necessary methods
        """
        self._repo = repo

    def add_book(self, id: str, author: str, title: str):
        """
        Adds a book to the repository. Returns a success or error message.
        :param id: the unique identifier
        :param author: the author of the book
        :param title: the title of the book
        :return: success or error message
        """
        book = Book(id, author, title)
        try:
            self._repo.add(book)
            return "Book added successfully."
        except DuplicateIDError:
            return f"Error: Book with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"

    def remove_book(self, id: str, rental_list: list,rental_repo):
        """
        Remove a book from the collection based on its unique identifier.
        :param rentallist:
        :param id: Unique identifier for the book that needs to be removed.
        :return:
        """
        try:
            for rental in rental_list:
                if rental.book_id == id:
                    rental_repo.remove(rental.id)
            self._repo.remove(id)
            return "Book removed successfully."
        except IDNotFoundError as ve:
            return f"Error: Book with ID {id} not found"

    def get_all(self) -> list:
        """
        Returns a list with all the books in the repository.
        :return: list of all books
        """
        return self._repo.get_all()

    def find(self,find_type: int, user_input: str):
        """
        Finds a book in the repo based on id/title/author
        :param find_type:
        :param user_input:
        :return:
        """
        if find_type == 1:
            try:
                return self._repo.find_by_id(user_input)
            except IDNotFoundError as ve:
                return f"Error: {str(ve)}"
        elif find_type == 2:
            try:
                return self._repo.find_by_title(user_input)
            except TitleNotFoundError as ve:
                return f"Error: {str(ve)}"
        elif find_type == 3:
            try:
                return self._repo.find_by_author(user_input)
            except AuthorNotFoundError as ve:
                return f"Error: {str(ve)}"

    def update(self, new_data, id):
        """
        Updates a book's information (title, author)'
        :param new_data:
        :param id:
        :return:
        """
        try:
            self._repo.update_book(id, new_data)
            return "Book updated successfully."
        except IDNotFoundError as idnfe:
            return f"Error: {str(idnfe)}"
        except ValidationException as ve:
            return f"Error: {str(ve)}"



    def undo_action(self):
        """
        Undo the last operation.
        :return: success or failure message
        """
        try:
            self._repo.undo()
        except Exception as e:
            print(f"Cannot undo: {str(e)}")
