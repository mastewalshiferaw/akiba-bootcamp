from typing import List, Optional
from book import Book
from member import Member


class Library:
    def __init__(self, name: str = "City Central Library"):
        self.name = name
        self._books: List[Book] = []
        self._members: List[Member] = []

    def add_book(self, book: Book):
        if self.find_book_by_isbn(book.isbn):
            print(f"Error: Book with ISBN {book.isbn} already exists.")
            return
        self._books.append(book)
        print(f"Book '{book.title}' added to library catalog.")

    def remove_book(self, isbn: str) -> bool:
        """Removes a book from the catalog by ISBN."""
        book = self.find_book_by_isbn(isbn)
        if book:
            if not book.is_available:
                print(f"Error: Cannot remove '{book.title}' because it is currently borrowed.")
                return False
            self._books.remove(book)
            print(f"Book '{book.title}' successfully removed.")
            return True
        print(f"Error: No book found with ISBN {isbn}.")
        return False

    def display_books(self):
        print(f"\n--- {self.name} Catalog ---")
        if not self._books:
            print("No books available in the library.")
            return
        for book in self._books:
            book.display_info()
        print("---------------------------------\n")

    def search_book(self, query: str):
        """Searches books by title, author, or ISBN."""
        query_lower = query.lower()
        matches = [
            b for b in self._books
            if query_lower in b.title.lower()
            or query_lower in b.author.lower()
            or query_lower in b.isbn.lower()
        ]
        if matches:
            print(f"\nFound {len(matches)} matching book(s):")
            for b in matches:
                b.display_info()
        else:
            print(f"No books found matching '{query}'.")

    def find_book_by_isbn(self, isbn: str) -> Optional[Book]:
    
        for b in self._books:
            if b.isbn.strip() == isbn.strip():
                return b
        return None

    def register_member(self, member: Member):
        if self.find_member_by_id(member.member_id):
            print(f"Error: Member with ID {member.member_id} is already registered.")
            return
        self._members.append(member)
        print(f"Member '{member.name}' registered as {member.__class__.__name__}.")

    def find_member_by_id(self, member_id: str) -> Optional[Member]:
        for m in self._members:
            if m.member_id.strip() == member_id.strip():
                return m
        return None

    def display_members(self):
        print("\n--- Registered Members ---")
        if not self._members:
            print("No members registered.")
            return
        for m in self._members:
            m.display_member_info()
        print("--------------------------\n")