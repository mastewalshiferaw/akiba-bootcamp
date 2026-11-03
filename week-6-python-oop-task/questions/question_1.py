class Student:

    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    
    def display_info(self):
        print(f"--- Student Details ---")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")

   
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am studying in the {self.department} department.\n")

student1 = Student("Alice Johnson", "CS101", "Computer Science")
student2 = Student("Brian Smith", "EE204", "Electrical Engineering")
student3 = Student("Clara Davis", "ME305", "Mechanical Engineering")


student1.display_info()
student1.introduce()

student2.display_info()
student2.introduce()

student3.display_info()
student3.introduce()

"""
What is a class in Python?
class is a blueprint for creating objects.

What is an object?
It is a concrete instance of a class containing real data.

What is the purpose of the __init__() method?
The constructor method that automatically initializes an object's attributes when created.

What is the difference between an attribute and a method?
 An attribute is a variable storing data (state); a method is a function performing an action (behavior).
 
"""