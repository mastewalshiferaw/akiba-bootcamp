numbers = []
total=0
count_odd=0
count_even=0

print("Please enter 10 numbers:")

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num) 
    total+=num
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1


average=total/10



smallest = min(numbers)
largest = max(numbers)

print(f"The Largest number is {largest}")
print(f"The Smallest number is {smallest}")
print(f"The Total sum of the numbers is: {total}")
print(f"The average of all the numbers is {average}")
print(f"Total even numbers: {count_even}")
print(f"Total odd numbers: {count_odd}")