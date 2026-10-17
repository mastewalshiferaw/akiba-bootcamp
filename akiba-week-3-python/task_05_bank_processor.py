account = {"balance": 100, "transactions": []}

def deposit(account, amount):
    if amount <= 0:
        return f"ERROR! deposit more than 0"
    account["balance"]+=amount

    receipt = {
        "type": "deposit",
        "amount": amount,
        "balance_after": account["balance"],
    }
    account["transactions"].append(receipt)

    return f"Successfully deposited {amount} birr. New balance: {account["balance"]}"

def withdraw(account, amount):
    if amount>account["balance"] or amount<=0:
        return f"can't withdraw more than your balance"

    account["balance"]=account["balance"]-amount

    receipt = {
            "type": "withdraw",
            "amount": amount,
            "balance_after": account["balance"],
        }

    account["transactions"].append(receipt)

    return account["balance"]

def check_balance(account):
    return account["balance"]

def generate_summary(account):
    """Calculates totals and displays the full transaction statement."""
    total_deposited = 0
    total_withdrawn = 0

    
    for item in account["transactions"]:
        if item["type"] == "deposit":
            total_deposited += item["amount"]
        elif item["type"] == "withdraw":
            total_withdrawn += item["amount"]

    
    print("\n" + "=" * 45)
    print("         BANK TRANSACTION STATEMENT         ")
    print("=" * 45)
    print(f"Total Deposited:  {total_deposited} ETB")
    print(f"Total Withdrawn:  {total_withdrawn} ETB")
    print(f"Final Balance:    {account['balance']} ETB")
    print(
        f"Remaining Limit:  {account['daily_limit'] - account['withdrawn_today']} ETB"
    )
    print("-" * 45)
    print("Transaction History:")