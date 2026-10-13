choice = input("Choose an option: ")

if choice == "1":
    print(f"\nYour current balance is: {balance} Birr\n")


elif choice == "2":
    deposit_amount = float(input("Enter deposit amount: "))
    
    if deposit_amount <= 0:
        print("\nDeposit amount must be greater than zero.\n")
    else:
        balance += deposit_amount
        transaction_count += 1
        print("Deposit successful!")
        print(f"Your new balance is: {balance} Birr\n")


elif choice == "3":
    withdrawal_amount = float(input("Enter withdrawal amount: "))
    
    if withdrawal_amount <= 0:
        print("\nWithdrawal amount must be greater than zero.\n")
    elif withdrawal_amount > balance:
        print("\nInsufficient balance!\n")
    else:
        balance -= withdrawal_amount
        transaction_count += 1
        print("Withdrawal successful!")
        print(f"Your new balance is: {balance} Birr\n")


elif choice == "4":
    print("\nThank you for using Akiba Bank!")
    print("Goodbye!")
    break


else:
    print("\nInvalid option.")
    print("Please choose a valid option.\n")