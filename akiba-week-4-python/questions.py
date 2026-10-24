#Question 1: Mutable and Immutable Objects
 
#Mutable objects: Can be changed after they are created without creating a new object (e.g., list, dict, set).

#Immutable objects: Cannot be changed once created. Any operation that seems to modify them actually creates a brand-new object in memory (e.g., str, int, float, tuple).


# Mutable example
my_list = [1, 2, 3] 
my_list.append(4)  
print("List:", my_list) #[1,2,3,4]

# Immutable
my_str = "hello"
#my_str[0] = "H"  #Why Error?!
new_str = my_str + " world"  # Creates a new string instead
print("Original string:", my_str)
print("New string:", new_str)

#Question 2: References and Object Identity
a = [10, 20, 30] 
b = a
c = [10, 20, 30]

#identity equality..is
print(a is b) #true
print(a is c) #false
print(a == c) #true

#"is" shows that our variable take that specific memory adress with equal value. Pointing to the same specfic memory. whereas "==" is equal value assigning. Like it shows us that the two values are equel

#a and c have the same values but they are different because they are on different memory location

#Question 3: Shared References and side effects
#Consider the following code:
numbers = [1, 2, 3]
values = numbers

values.append(4)

print(numbers) #[1,2,3,4]
print(values)#[1,2,3,4]
'''
Answer the following:
modifying values affect the numbers because they variables points to the same memory and changing one have impact on all the value pointing out that memory

we can rewrite as values==numbers
'''


#question number 4: function arguments and mutability

def update_list(items):
    items.append(100)

scores = [50, 60, 70]
update_list(scores)

print(scores) #the output will be 

def update_list(items):
    # Create a new independent copy using slicing [:]
    new_items = items[:]
    new_items.append(100)
    return new_items


scores = [50, 60, 70]
new_scores = update_list(scores)

print("Original scores:", scores)  # Remains [50, 60, 70]
print("New scores:", new_scores)  # Becomes [50, 60, 70, 100]

#question number 5

my_list = [10, 20, 30]


another_list = my_list


del my_list


print(another_list)

#Question 5: Memory Management and Garbage Collection