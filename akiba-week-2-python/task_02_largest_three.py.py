num_1=int(input("Enter a number: "))
num_2 = int(input("second number: "))
num_3= int(input("Third number: "))

if num_1==num_2==num_3:
    print(f"All the three numbers are equal.")

elif num_1==num_2 and num_1>num_3:
     print(f"{num_1} and {num_2} are equal numbers")
elif num_2==num_3 and num_2>num_1:
     print(f"{num_1} and {num_2} are equal numbers")

elif num_2>=num_1 and num_2>=num_3:
     print(f"{num_2} is the largest")

elif num_3>=num_2 and num_3>=num_1:
     print(f"{num_3} is the largest of all.")


else:
     print(f"{num_1} is the largest.")



