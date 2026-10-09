user_start = int(input("Starting number: "))
user_ending = int(input("Ending number: "))

for i in range (user_start, user_ending+1):
    if i%3==0 and i%5==0:
            print("FizzBuzz")
    elif i%3==0:
        print("Fizz")

    elif i%5==0:
        print("Buzz")


    else:
        print(i)
