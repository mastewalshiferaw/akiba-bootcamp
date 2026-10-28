# ==========================
# Task 1: Student Information System
# ==========================

class Student:
    
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print("-" * 30)



student1 = Student("Alice Johnson", 20, "Computer Science")
student2 = Student("Brian Smith", 22, "Mechanical Engineering")
student3 = Student("Clara Davis", 21, "Data Science")


print("--- Student Information System ---")
student1.display_info()
student2.display_info()
student3.display_info()