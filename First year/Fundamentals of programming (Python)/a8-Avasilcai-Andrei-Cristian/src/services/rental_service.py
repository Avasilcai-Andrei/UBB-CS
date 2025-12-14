from src.domain.rental import Rental
from datetime import datetime

from src.repository.memoery_repo import IDNotFoundError

dt = datetime.now()

class InvalidDateFromat(ValueError):
    def __init__(self, message="A date format error occurred"):
        super().__init__(message)
        self.message = message

class IDValidatorException(KeyError):
    def __init__(self, message="A validation error occurred"):
        super().__init__(message)
        self.message = message

class ValidationException(Exception):
    def __init__(self, message = "A validation error occurred"):
        super().__init__(message)
        self.message = message

class RentalService:
    def __init__(self, repo):
        """
        The repo parameter is the repository passed from outside (e.g., MemoryRepository)
        :param repo: Repository-like object that implements the necessary methods
        """
        self._repo = repo

    @property
    def repo(self):
        return self._repo

    def is_book_available(self, book_id, start_date, end_date):
        """Check if a book is available for rental during the given dates."""
        for rental in self._repo.get_all():
            if rental.book_id == book_id:
                if end_date >= rental.rented_date or start_date <= rental.return_date:
                    return False
        return True

    def add_rental(self, id: str, book_id: str, client_id: str, rented_date: str, return_date : str, booklist, clientlist):
        """
        Adds a rental to the repository
        :param clientlist:
        :param booklist:
        :param id:
        :param book_id:
        :param client_id:
        :param rented_date:
        :param return_date:
        :return:
        """
        if not any(book.id == book_id for book in booklist):
            return f"Error: Book with ID {book_id} not found"
        if not any(client.id == client_id for client in clientlist):
            return f"Error: Client with ID {client_id} not found"
        try:
            rented_date = datetime.strptime(rented_date, "%d/%m/%Y").date()
            return_date = datetime.strptime(return_date, "%d/%m/%Y").date()
            if rented_date > return_date:
                return "Error: Rented date cannot be after return date."
            if self.is_book_available(book_id, rented_date, return_date):
                rental = Rental(id, book_id, client_id, rented_date, return_date)
                self._repo.add(rental)
                return "Rental added successfully."
            else:
                return f"Error: Book with ID {book_id} is not available for rental."
        except IDValidatorException:
            return f"Error: Rental with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"
        except InvalidDateFromat as ide :
            return "Error: Invalid date format. Use the following format: DD/MM/YYYY."

    def remove_rental(self, id: str):
        """
        Remove a rental from the collection based on its unique identifier.
        :param id: Unique identifier for the rental that needs to be removed.
        :return:
        """
        try:
            self._repo.remove(id)
            return "Rental removed successfully."
        except IDValidatorException:
            return f"Error: Rental with ID {id} not found"
        except IDNotFoundError as idnfe:
            return f"Error: {str(idnfe)}"

    def get_all(self) -> list:
        """
        Returns a list with all the rentals in the repository.
        :return: list of all clients
        """
        return self._repo.get_all()

    def undo_action(self):
        """
        Undo the last operation.
        :return: success or failure message
        """
        try:
            self._repo.undo()
        except Exception as e:
            print(f"Cannot undo: {str(e)}")
