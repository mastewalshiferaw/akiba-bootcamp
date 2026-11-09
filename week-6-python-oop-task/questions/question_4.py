#Part A: Polymorphism
# Define the classes with the same method name: make_sound()
class Dog:
    def make_sound(self):
        return "Woof! Woof!"


class Cat:
    def make_sound(self):
        return "Meow!"


class Cow:
    def make_sound(self):
        return "Moo!"


# objects
dog = Dog()
cat = Cat()
cow = Cow()

# Demonstrate polymorphism
# The same method call works across different object types
animals = [dog, cat, cow]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.make_sound()}")

#Part B: Abstraction

import math
from abc import ABC, abstractmethod


# Abstract Base Class
class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        """Abstract method that all child classes must implement."""
        pass


# Child class 1: Rectangle
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# Child class 2: Circle
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius**2)


#objects andtheir calculated areas
rect = Rectangle(length=10, width=5)
circ = Circle(radius=7)

print(f"Rectangle Area: {rect.calculate_area()}")
print(f"Circle Area: {circ.calculate_area():.2f}")

"""
Answers to Theory Questions
1. What is polymorphism?
Polymorphism means "many forms". In OOP, it refers to the ability of different classes to have methods with the same name, allowing code to treat them interchangeably while each class executes its own specific behavior (as seen with animal.make_sound()).

2. What is abstraction?
Abstraction is the concept of hiding complex internal implementation details and showing only the essential features to the user. Users only need to know what an object does, not how it does it internally.

3. What is an abstract class?
An abstract class is a class designed to be a blueprint for other classes. It cannot be directly instantiated (you cannot create an object directly from it) and typically contains one or more abstract methods that child classes are required to define.

4. What happens if a child class does not implement an inherited abstract method?
If a child class fails to implement an abstract method:
The child class itself remains an abstract class.
If you try to instantiate (create an object of) that child class, Python will raise a runtime error:
TypeError: Can't instantiate abstract class ... with abstract method ...

5.What is the difference between abstraction and encapsulation?
Abstraction hides complexity; encapsulation protects data.
"""