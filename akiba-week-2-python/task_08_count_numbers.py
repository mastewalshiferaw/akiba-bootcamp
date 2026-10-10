num=int(input("Enter a postive number: "))
even=0
odd=0
total=0

for _ in range (1, num+1):
    
    if _%2==0:
        even+=1
    else:
        odd+=1

    total+=_

print(f"total even numbers: {even}")
print(f"total odd numbers: {odd}")
print(f"The sum of all numbers is: {total}")

