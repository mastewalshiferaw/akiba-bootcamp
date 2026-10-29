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


