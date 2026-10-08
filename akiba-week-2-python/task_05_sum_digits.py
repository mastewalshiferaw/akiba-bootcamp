num=int(input("Enter a number: "))
total = 0

while num > 0:
    last = num%10
    total+=last

    num = num//10

print(total)
