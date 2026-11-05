# Parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")


# Child class: Manager
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Manager: {self.name}, Salary: ${self.salary}, Department: {self.department}")


# Child class: Developer
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        print(f"Developer: {self.name}, Salary: ${self.salary}, Language: {self.programming_language}")


# Create objects
emp = Employee("Alice", 50000)
mgr = Manager("Bob", 85000, "Engineering")
dev = Developer("Charlie", 75000, "Python")

# Call display_info for each object
emp.display_info()
mgr.display_info()
dev.display_info()


# ==========================================
# ANSWERS TO QUESTIONS
# ==========================================

# 1. What is inheritance?
# A mechanism where a child class acquires the attributes and methods of a parent class to promote code reusability.

# 2. What is the difference between a parent class and a child class?
# A parent class (base class) defines common attributes and methods, while a child class (subclass) inherits from the parent and can add or modify features.

# 3. What is method overriding?
# Redefining a parent class method inside a child class with the same name to provide class-specific implementation.

# 4. What is the purpose of super()?
# It allows a child class to call and access the constructor (__init__) and methods of its parent class.

# 5. What is the difference between single and multiple inheritance?
# Single inheritance involves a child class inheriting from only one parent class, while multiple inheritance involves a child class inheriting from more than one parent class.