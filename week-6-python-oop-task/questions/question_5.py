class Product:
    store_name = "TechMart"

    def __init__(self, name: str, price: float):
        if not Product.is_valid_price(price):
            raise ValueError(f"Invalid price: {price}. Price must be greater than zero.")
        self.name = name
        self.price = price

    def display_product(self):
        print(f"Product: {self.name} | Price: ${self.price:.2f} | Store: {Product.store_name}")

    @classmethod
    def change_store_name(cls, new_name: str):
        cls.store_name = new_name
        print(f"Store name successfully updated to: {cls.store_name}")

    @staticmethod
    def is_valid_price(price: float) -> bool:
        return isinstance(price, (int, float)) and price > 0


class ShoppingCart:
    
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
       
        if isinstance(product, Product):
            self.products.append(product)
            print(f"Added '{product.name}' to the cart.")
        else:
            print("Error: Only Product objects can be added.")

    def calculate_total(self) -> float:
        
        return sum(item.price for item in self.products)

    def display_cart(self):
        
        print("\n--- Shopping Cart Items ---")
        if not self.products:
            print("Your cart is empty.")
            return

        for index, item in enumerate(self.products, start=1):
            print(f"{index}. {item.name} - ${item.price:.2f}")

        total = self.calculate_total()
        print(f"Total Amount: ${total:.2f}")
        print("---------------------------\n")



if __name__ == "__main__":
    print("=== Testing Static Method ===")
    print(f"Is $45.00 valid? {Product.is_valid_price(45.00)}")
    print(f"Is -$10.00 valid? {Product.is_valid_price(-10.00)}")

    print("\n=== Creating Products ===")
    p1 = Product("Laptop", 999.99)
    p2 = Product("Mouse", 25.50)
    p3 = Product("Keyboard", 60.00)

    p1.display_product()
    p2.display_product()

    print("\n=== Changing Store Name (Class Method) ===")
    Product.change_store_name("MegaTech Superstore")
    p1.display_product()

    print("\n=== Shopping Cart (Composition) ===")
    cart = ShoppingCart()
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)

    cart.display_cart()

"""
THEORETICAL ANSWERS

1. What is the difference between instance attributes and class attributes?
   - Instance Attributes: Variables bound to a specific instance of a class via `self`. 
     Each object maintains its own independent copy (e.g., product name or price).
   - Class Attributes: Variables defined directly inside the class body and shared by 
     all instances of that class (e.g., store_name). Modifying it at the class level reflects 
     across all instances.

2. What is an instance method?
   - A function defined inside a class that takes `self` as its first parameter. It operates 
     on individual object instances and can access or modify instance state as well as class state.

3. What is a class method?
   - A method decorated with `@classmethod` that receives the class itself (`cls`) as its 
     first argument instead of an instance (`self`). It can modify class-level state that applies 
     across all instances.

4. What is a static method?
   - A method decorated with `@staticmethod` that takes neither `self` nor `cls` as an implicit 
     first argument. It behaves like a plain utility function housed inside the class's namespace.

5. What is the difference between composition and inheritance?
   - Inheritance represents an "IS-A" relationship (e.g., Developer is an Employee). A subclass 
     inherits behavior and state from a superclass.
   - Composition represents a "HAS-A" relationship (e.g., ShoppingCart has Products). A class 
     contains references to objects of other classes as part of its data, promoting loose coupling.
"""