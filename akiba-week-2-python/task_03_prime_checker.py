num = int(input("Enter a number: "))

if num<=1:
    print("not prime")
else:
    for i in range(2, int(num**0.5)+1):
        #We don't need to check up to num because we get pairs of number as in every divisor and that goes up to the square root of that number
        if num%i == 0:
            print("not prime")
            break
    else:
        print("Prime")