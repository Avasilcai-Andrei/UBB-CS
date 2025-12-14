from src.domain.client import Client
from src.repository.memoery_repo import IDNotFoundError
from src.repository.memoery_repo import DuplicateIDError,NameNotFoundError

class IDValidatorException(KeyError):
    def __init__(self, message="A validation error occurred"):
        super().__init__(message)
        self.message = message

class ValidationException(Exception):
    def __init__(self, message = "A validation error occurred"):
        super().__init__(message)
        self.message = message

class ClientService:
    def __init__(self, repo):
        """
        The repo parameter is the repository passed from outside (e.g., MemoryRepository)
        :param repo: Repository-like object that implements the necessary methods
        """
        self._repo = repo

    def add_client(self, id: str, name: str):
        """
        Adds a client to the repository. Returns a success or error message.
        :param id: the unique identifier
        :param name: the name of the client
        :return: success or error message
        """
        client = Client(id, name)
        try:
            self._repo.add(client)
            return "Client added successfully."
        except DuplicateIDError:
            return f"Error: Client with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"

    def remove_client(self, id: str, rental_list: list, rental_repo):
        """
        Remove a client from the collection based on its unique identifier.
        :param rentallist:
        :param id: Unique identifier for the client that needs to be removed.
        :return:
        """
        try:
            for rental in rental_list:
                if rental.client_id == id:
                    rental_repo.remove(rental.id)
            self._repo.remove(id)
            return "Client removed successfully."
        except IDNotFoundError:
            return f"Error: Client with ID {id} not found"

    def get_all(self) -> list:
        """
        Returns a list with all the clients in the repository.
        :return: list of all clients
        """
        return self._repo.get_all()

    def find(self,find_type: int, user_input: str):
        """
        Searches for a client in the repo based on id/name
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
                return self._repo.find_by_name(user_input)
            except NameNotFoundError as ve:
                return f"Error: {str(ve)}"

    def update(self, new_data, id):
        """
        Updates a client's information (name)
        :param new_data:
        :param id:
        :return:
        """
        try:
            self._repo.update_client(id, new_data)
            return "Client updated successfully."
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
