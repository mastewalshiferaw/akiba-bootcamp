class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder  
        self.__balance = initial_balance      

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.2f}")

    def get_balance(self):
        print(f"Current balance: ${self.__balance:.2f}")
        return self.__balance



if __name__ == "__main__":
  
    account = BankAccount("Alice", initial_balance=100.0)

    print(f"Account Holder: {account.account_holder}")

    account.get_balance()

    account.deposit(50.0)
    account.get_balance()

    account.withdraw(30.0)
    account.get_balance()

    
    account.withdraw(200.0)

    try:
        print(account.__balance)
    except AttributeError as e:
        print(f"\nEncapsulation check: Cannot access '__balance' directly ({e}).")


"""
What is encapsulation?
Encapsulation is the OOP concept of bundling data (attributes) and methods that operate on that data inside a single unit (class), while restricting direct outside access to internal details.

Why do we use private attributes?
To protect sensitive data from accidental modification, prevent unwanted direct access from outside the class, and enforce validation rules via methods.

What is name mangling in Python?
It is Python’s automatic mechanism that renames an attribute with two leading underscores (e.g., __balance) to _ClassName__balance internally, preventing name clashes in subclasses and accidental direct access.

Difference between public, protected, and private naming conventions:
Public (name): Accessible from anywhere (inside and outside the class).

Protected (_name): Single leading underscore; a developer convention meaning "intended for internal and subclass use only" (not enforced by Python).

Private (__name): Double leading underscore; enforces name mangling to prevent direct access from outside the class.
"""