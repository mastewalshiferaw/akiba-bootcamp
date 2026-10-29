class Product:
    
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self) -> float:
        return self.price * self.quantity


    def __str__(self) -> str:
        return (
            f"Product: {self.name} | "
            f"Price: ${self.price:.2f} | "
            f"Quantity: {self.quantity} | "
            f"Total Inventory Value: ${self.total_value():.2f}"
        )



product1 = Product("Laptop", 999.99, 10)
product2 = Product("Wireless Mouse", 24.50, 50)
product3 = Product("Mechanical Keyboard", 89.00, 25)


print("--- Product Catalog ---")
print(product1)
print(product2)
print(product3)

