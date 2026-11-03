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