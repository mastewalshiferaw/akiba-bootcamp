# Practical Mini-Project: Library Management System

## Overview
A modular, console-based Library Management System developed using Python and Object-Oriented Programming (OOP) principles. It manages books and members while enforcing borrowing rules and limits.

## Project Structure
- `book.py`: Defines the `Book` class with encapsulated attributes (`_title`, `_author`, `_isbn`, `__is_available`) and accessors.
- `member.py`: Defines base class `Member` and derived classes `StudentMember` and `TeacherMember` with overridden borrowing limits.
- `library.py`: Manages the collection of books and members using composition.
- `main.py`: Command-line interface offering an interactive menu for all library operations.

---

## Project Reflection Answers

### 1. Where did you use inheritance?
Inheritance is implemented in `member.py`:
- `Member` serves as the parent class providing shared attributes (`name`, `member_id`, `_borrowed_books`) and core logic (`borrow_book`, `return_book`, `display_member_info`).
- `StudentMember` and `TeacherMember` inherit from `Member` using `super().__init__(name, member_id)` to reuse the parent initialization logic.

### 2. How did you implement encapsulation?
- In `Book`, the attribute `__is_available` is kept private using double-underscore name mangling. It cannot be altered directly from outside; instead, access is regulated via the `@property` getter and `set_availability()` method.
- In `Member`, `_borrowed_books` is protected, and interactions are managed strictly through `borrow_book()` and `return_book()`.

### 3. Where did you demonstrate polymorphism?
Polymorphism is demonstrated through method overriding in `StudentMember` and `TeacherMember`:
- Both child classes override the `get_borrow_limit()` method:
  - `StudentMember.get_borrow_limit()` returns `3`.
  - `TeacherMember.get_borrow_limit()` returns `5`.
- In `main.py`, `member.borrow_book(book)` dynamically invokes the correct borrowing limit based on the runtime type of `member` without requiring type inspection.

### 4. How did your classes interact with each other?
The system utilizes **composition** and **association**:
- `Library` has-a collection of `Book` and `Member` objects.
- `Member` maintains a list of `Book` objects that are currently borrowed.
- When a member borrows a book, `Member.borrow_book()` updates both the member's list and calls `Book.set_availability(False)` to change the book's state.

### 5. Why is OOP useful when developing large software applications?
- **Modularity**: Code is partitioned into distinct, reusable files and classes.
- **Maintainability & Extensibility**: New member types (e.g., `StaffMember`) or media types (e.g., `Audiobook`) can be added without rewriting existing logic.
- **Data Integrity**: Encapsulation ensures that invalid states (such as duplicate checkouts or exceeding borrowing limits) are prevented by design.