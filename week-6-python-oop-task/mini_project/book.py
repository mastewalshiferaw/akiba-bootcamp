class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self._title = title
        self._author = author
        self._isbn = isbn
        # Private attribute 
        self.__is_available = True


    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def is_available(self):
        return self.__is_available

    def set_availability(self, status: bool):
        self.__is_available = status

    def display_info(self):
       
        status = "Available" if self.__is_available else "Borrowed"
        print(f"ISBN: {self._isbn} | Title: '{self._title}' | Author: {self._author} | Status: {status}")

    def __str__(self):
        return f"'{self._title}' by {self._author} (ISBN: {self._isbn})"