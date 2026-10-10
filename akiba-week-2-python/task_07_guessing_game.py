secret_number = 32
user_input = int(input("Input a number: "))

if user_input==secret_number:
        print("Congratulations!\nYou guessed the number in 1 attempt.")
else:
    for i in range (2, 6):
        user_input = int(input("Input a number: "))
        if user_input==secret_number:
            print(f"Congratulations!\nYou guessed the number in {i} attempts.")
            
            break

    else:
         print("Game over!")



        
        


