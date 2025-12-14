from src.repository.memory_repo import MemoryRepository
from src.repository.text_repo import TextFileRepository
from src.repository.binary_repo import BinaryRepository
from src.services.book_service import BookService
from src.ui.ui import UI
from src.domain.book import Book
from tests import run_all_tests
from faker import Faker

fake = Faker()

def generate_random_books(num_books=10):
    """Generate a list of random books."""
    books = []
    for _ in range(num_books):
        isbn = fake.isbn13()
        author = fake.name()
        title = fake.catch_phrase()
        books.append(Book(isbn, author, title))
    return books

def populate_repo_with_random_books(repo, num_books=10):
    """Populate the repository with randomly generated books."""
    books = generate_random_books(num_books)
    for book in books:
        repo._data[book.isbn] = book
    repo.save_state()

def main():
    run_all_tests()
    #repo = MemoryRepository()
    repo = TextFileRepository("books.txt")
    #repo = BinaryRepository("book_data.pickle")
    if len(repo) == 0:
        populate_repo_with_random_books(repo)
    service = BookService(repo)
    ui = UI(service)
    ui.run()

if __name__ == "__main__":
    main()
