from book import Book


class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self._borrowed_books = []

    @property
    def borrowed_books(self):
        return self._borrowed_books

    def get_borrow_limit(self):
        return 2

    def borrow_book(self, book: Book):
        if not book.is_available:
            print(f"Error: {book} is currently not available.")
            return False

        if len(self._borrowed_books) >= self.get_borrow_limit():
            print(f"Limit reached: {self.name} cannot borrow more than {self.get_borrow_limit()} books.")
            return False

        self._borrowed_books.append(book)
        book.set_availability(False)
        print(f"Success: {self.name} borrowed {book}.")
        return True

    def return_book(self, book: Book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.set_availability(True)
            print(f"Success: {self.name} returned {book}.")
            return True
        else:
            print(f"Error: {self.name} does not have {book} on loan.")
            return False

    def display_member_info(self):
        print(f"ID: {self.member_id} | Name: {self.name} | Role: {self.__class__.__name__} | Borrow Limit: {self.get_borrow_limit()}")
        if self._borrowed_books:
            print("  Borrowed Books:")
            for b in self._borrowed_books:
                print(f"    - {b.title} (ISBN: {b.isbn})")
        else:
            print("  No books currently borrowed.")


class StudentMember(Member):
    def __init__(self, name: str, member_id: str):
        super().__init__(name, member_id)

    # Method Overriding
    def get_borrow_limit(self) -> int:
        return 3


class TeacherMember(Member):
    def __init__(self, name: str, member_id: str):
        super().__init__(name, member_id)

    # Method Overriding
    def get_borrow_limit(self):
        return 5