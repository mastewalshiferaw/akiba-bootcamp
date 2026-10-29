# ==========================
# Task 1: Student Information System
# ==========================

class Student:
    
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print("-" * 30)



student1 = Student("Alice Johnson", 20, "Computer Science")
student2 = Student("Brian Smith", 22, "Mechanical Engineering")
student3 = Student("Clara Davis", 21, "Data Science")


print("--- Student Information System ---")
student1.display_info()
student2.display_info()
student3.display_info()

# ==========================
# Task 2:  Rectangle Calculator
# ==========================

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"


rectangle1 = Rectangle(5, 4)
r2 = Rectangle(3,4)

print(rectangle1)

print("AREA(Rectangle 1):", rectangle1.area())
print("Perimeter(Rectangle 1):", rectangle1.perimeter())

print(r2)
print("AREA(Rectangle 2):", r2.area())
print("Perimeter(Rectangle 2):", r2.perimeter())

# ==========================
# Task 3:  Student Score Management
# ==========================

class Student:
    school_name = "Akiba Academy"

    def __init__(self, name, score, department):
        self.name = name
        self.score = score
        self.department = department

    def display(self):
        print(f"Student Details:")
        print(f"  School: {Student.school_name}")
        print(f"  Name:   {self.name}")
        print(f"  Dept:   {self.department}")
        print(f"  Score:  {self.score}")
        print("-" * 20)

student1 = Student("Abebe", 88, "Mathematics")
student2 = Student("chal", 92, "Physics")
student3 = Student("merga", 75, "Chemistry")

print("--- Initial State ---")
student1.display()
student2.display()
student3.display()

print("--- Updating chala Score ---")
student2.score = 98 
student2.display()

print("--- Verification of Independence ---")
print(f"{student1.name}'s score: {student1.score}")
print(f"{student2.name}'s score: {student2.score}")
print(f"{student3.name}'s score: {student3.score}")
'''
Questions:
What is the difference between a class attribute and an instance attribute?

well is the difference between them is that class attribute is shared by all instances of a class, whereas instance attribute is unique to the individual object created.
Why does updating one student's score not automatically change the scores of other students?

Scores are defined as instance attributes (self.score). When Python creates an object, it allocates a unique memory location for that object and its specific attributes.

'''

# ==========================
# Task 4: Product Information System
# ==========================
class Product:
    
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


    def __str__(self):
        return (
            f"Product: {self.name} | "
            f"Price: ${self.price:.2f} | "
            f"Quantity: {self.quantity} | "
            f"Total Inventory Value: ${self.total_value():.2f}"
        )



product1 = Product("Laptop", 999.99, 10)
product2 = Product("Wireless Mouse", 24.50, 50)
product3 = Product("Mechanical Keyboard", 89.00, 25)


print("--- Product Catalog ---")
print(product1)
print(product2)
print(product3)


# ==========================
# Task 5: Bank Account Management
# ==========================

class BankAccount:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        if amount<=0:
            print("DEPOSITIED AMOUNT MUST BE GREATER THAN 0.")

        else:
            self.balance += amount

            print(f"Deposited {amount} birr.")

    def withdraw(self, amount):
        if amount>self.balance and amount<0:
            print("CANNOT WITHDRAW!")
        else:
            self.balance-=amount
            print(f"Withdraw {amount} birr.")

    def display_balance(self):
        print(f"{self.owner} balance: {self.balance} birr.")


print("Account 1")
account1=BankAccount("Mignot", 10000)

account1.deposit(2000)
account1.withdraw(400)
account1.display_balance()

print("Account 2")
account2=BankAccount("Liza", 5000)

account2.deposit(2000)
account2.withdraw(400)
account2.display_balance()


