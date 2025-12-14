class UI:
    def __init__(self, service):
        self._service = service

    def printMenu(self):
        print("1. Add book")
        print("2. Display all books")
        print("3. Filter by a given word")
        print("4. Undo")
        print("5. Exit")

    def run(self):
        while True:
            self.printMenu()
            choice = input("Choose an option: ")

            if choice == '1':
                isbn = input("Enter ISBN: ")
                author = input("Enter author: ")
                title = input("Enter title: ")
                self.add_book(isbn, author, title)
            elif choice == '2':
                self.display_books()
            elif choice == '3':
                word = input("Enter the word to filter by: ")
                self.filter_books(word)
            elif choice == '4':
                self.undo_action()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid option! Please try again.")

    def add_book(self, isbn, author, title):
        result = self._service.add_book(isbn, author, title)
        print(result)

    def display_books(self):
        books = self._service.get_all()
        if books:
            print("Books in the repository:")
            for book in books:
                print(book)
        else:
            print("No books in the repository.")

    def filter_books(self, word):
        result = self._service.filter_books(word)
        print(result)

    def undo_action(self):
        result = self._service.undo_action()
