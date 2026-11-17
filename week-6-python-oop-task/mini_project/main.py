from book import Book
from library import Library
from member import StudentMember, TeacherMember


def seed_initial_data(library: Library):
    b1 = Book("Clean Code", "Robert C. Martin", "978-0132350884")
    b2 = Book("Python Crash Course", "Eric Matthes", "978-1593279288")
    b3 = Book("Design Patterns", "Erich Gamma et al.", "978-0201633610")
    b4 = Book("Fluent Python", "Luciano Ramalho", "978-1491946008")

    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)
    library.add_book(b4)

    m1 = StudentMember("Alice Johnson", "S101")
    m2 = TeacherMember("Dr. John Smith", "T201")

    library.register_member(m1)
    library.register_member(m2)


def print_menu():
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Register Member")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Display All Members")
    print("8. Exit")


def main():
    library = Library("Akiba Community Library")
    seed_initial_data(library)

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            isbn = input("Enter ISBN: ").strip()
            if title and author and isbn:
                library.add_book(Book(title, author, isbn))
            else:
                print("Error: All fields are required.")

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            query = input("Enter book title, author, or ISBN to search: ").strip()
            if query:
                library.search_book(query)
            else:
                print("Error: Search query cannot be empty.")

        elif choice == "4":
            name = input("Enter member name: ").strip()
            member_id = input("Enter member ID: ").strip()
            print("Select Member Type:")
            print("1. Student (Borrow limit: 3)")
            print("2. Teacher (Borrow limit: 5)")
            m_type = input("Choice (1-2): ").strip()

            if m_type == "1":
                member = StudentMember(name, member_id)
                library.register_member(member)
            elif m_type == "2":
                member = TeacherMember(name, member_id)
                library.register_member(member)
            else:
                print("Invalid member type selected.")

        elif choice == "5":
            member_id = input("Enter member ID: ").strip()
            member = library.find_member_by_id(member_id)
            if not member:
                print(f"Error: Member with ID '{member_id}' not found.")
                continue

            isbn = input("Enter book ISBN to borrow: ").strip()
            book = library.find_book_by_isbn(isbn)
            if not book:
                print(f"Error: Book with ISBN '{isbn}' not found.")
                continue

        
            member.borrow_book(book)

        elif choice == "6":
            member_id = input("Enter member ID: ").strip()
            member = library.find_member_by_id(member_id)
            if not member:
                print(f"Error: Member with ID '{member_id}' not found.")
                continue

            isbn = input("Enter book ISBN to return: ").strip()
            book = library.find_book_by_isbn(isbn)
            if not book:
                print(f"Error: Book with ISBN '{isbn}' not found in library registry.")
                continue

            member.return_book(book)

        elif choice == "7":
            library.display_members()

        elif choice == "8":
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid number (1-8).")


if __name__ == "__main__":
    main()