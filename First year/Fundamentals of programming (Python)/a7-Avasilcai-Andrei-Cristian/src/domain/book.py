class Book(object):
    def __init__(self, isbn: str, author: str, title: str):
        self.__isbn = isbn
        self.__author = author
        self.__title = title

    @property
    def isbn(self):
        return self.__isbn

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @author.setter
    def author(self, new_author):
        self.__author = new_author

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    def __eq__(self, other):
        if type(other) != Book:
            return False
        return self.isbn == other.isbn

    def __str__(self):
        return f"ISBN: {self.isbn}, Author: {self.author}, Title: {self.title}"

    def __repr__(self):
        return str(self)
