pin="1234"
attempts_remaining = 3

while attempts_remaining > 0:
    correct=input("Enter the correct PIN: " )
    if correct==pin:
        print("Verified!")
        break
    else:
        attempts_remaining-=1
        if attempts_remaining > 0:
            print("Incorrect PIN.")
            print(f"Attempts remaining: {attempts_remaining}")
        else:
            print("Incorrect PIN.")
            print("Maximum attempts reached.")
        