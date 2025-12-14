from src.repository.memory_repo import MemoryRepository
from src.domain.book import Book
from src.services.book_service import BookService

def test_book_creation():
    """Test creating a book and updating its fields."""
    book = Book("978-0132350884", "Robert C. Martin", "Clean Code")
    assert book.isbn == "978-0132350884", f"Expected ISBN '978-0132350884', got {book.isbn}"
    assert book.author == "Robert C. Martin", f"Expected author 'Robert C. Martin', got {book.author}"
    assert book.title == "Clean Code", f"Expected title 'Clean Code', got {book.title}"
    book.author = "Martin Robert C."
    assert book.author == "Martin Robert C.", f"Expected author 'Martin Robert C.', got {book.author}"
    book.title = "Clean Code - New Edition"
    assert book.title == "Clean Code - New Edition", f"Expected title 'Clean Code - New Edition', got {book.title}"

def test_add_book_to_repository():
    """Test adding books to the repository and verifying the repository contents."""
    try:
        repo = MemoryRepository()
        book1 = Book("978-0132350884", "Robert C. Martin", "Clean Code")
        repo.add(book1)
        books = repo.get_all()
        assert len(books) == 1, f"Expected 1 book, found {len(books)}"
        assert books[0].isbn == "978-0132350884", f"Expected ISBN '978-0132350884', got {books[0].isbn}"
        assert books[0].author == "Robert C. Martin", f"Expected author 'Robert C. Martin', got {books[0].author}"
        assert books[0].title == "Clean Code", f"Expected title 'Clean Code', got {books[0].title}"
        book2 = Book("978-0201616224", "Martin Fowler", "Refactoring")
        repo.add(book2)
        books = repo.get_all()
        assert len(books) == 2, f"Expected 2 books, found {len(books)}"
        assert books[1].isbn == "978-0201616224", f"Expected ISBN '978-0201616224', got {books[1].isbn}"
        assert books[1].author == "Martin Fowler", f"Expected author 'Martin Fowler', got {books[1].author}"
        assert books[1].title == "Refactoring", f"Expected title 'Refactoring', got {books[1].title}"
        assert books[0].isbn == "978-0132350884", f"Expected ISBN '978-0132350884', got {books[0].isbn}"

    except Exception as e:
        print(f"Error during test_add_book_to_repository: {e}")

def test_add_book_service():
    """Test adding books via the service and verify repository behavior."""
    try:
        repo = MemoryRepository()
        service = BookService(repo)
        result = service.add_book("978-0132350884", "Robert C. Martin", "Clean Code")
        assert result == "Book added successfully.", f"Expected 'Book added successfully.', got {result}"
        books = repo.get_all()
        assert len(books) == 1, f"Expected 1 book, found {len(books)}"
        assert books[0].isbn == "978-0132350884", f"Expected ISBN '978-0132350884', got {books[0].isbn}"
        result = service.add_book("978-0201616224", "Martin Fowler", "Refactoring")
        assert result == "Book added successfully.", f"Expected 'Book added successfully.', got {result}"
        books = repo.get_all()
        assert len(books) == 2, f"Expected 2 books, found {len(books)}"
        assert books[1].isbn == "978-0201616224", f"Expected ISBN '978-0201616224', got {books[1].isbn}"

    except Exception as e:
        print(f"Error during test_add_book_service: {e}")

def run_all_tests():
    """Run all tests."""
    try:
        test_book_creation()
        test_add_book_to_repository()
        test_add_book_service()
        print("All tests passed successfully.")
    except AssertionError as e:
        print(f"Test failed: {e}")

