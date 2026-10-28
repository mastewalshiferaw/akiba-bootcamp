class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"


rectangle1 = Rectangle(5, 4)
r2 = Rectangle(3,4)

print(rectangle1)

print("AREA(Rectangle 1):", rectangle1.area())
print("Perimeter(Rectangle 1):", rectangle1.perimeter())

print(r2)
print("AREA(Rectangle 2):", r2.area())
print("Perimeter(Rectangle 2):", r2.perimeter())

