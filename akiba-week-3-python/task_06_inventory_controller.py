inventory = [
    {"name": "Laptop", "price": 999.99, "stock": 10},
    {"name": "Mouse", "price": 25.0, "stock": 3}
]

def search_product(inventory, name):
    for item in inventory:
        if item["name"].lower() == name.strip().lower():
            return item
    return None

#new_product = {"name": name, "price": price, "stock": stock}
def add_product(inventory, name, price, stock):
    
    if not name or not name.strip():
        return "Error: Product name cannot be empty."

   
    if price < 0:
        return "Error: Price cannot be negative."
    if stock < 0:
        return "Error: Stock cannot be negative."

    if search_product(inventory, name) is not None:
        return f"Error: Product '{name}' already exists."

    new_product = {
        "name": name.strip(),
        "price": price,
        "stock": stock
    }
    inventory.append(new_product)
    return f"Success: Added '{name}'."

def update_product_price(inventory, name, new_price):
   
    product = search_product(inventory, name)
    if product is None:
        return f"Error: Product '{name}' not found."

    if new_price < 0:
        return "Error: Price cannot be negative."

    product["price"] = float(new_price)
    return f"Success: Updated price of '{product['name']}' to ${new_price:.2f}."


def increase_stock(inventory, name, quantity):
    product = search_product(inventory, name)
    if product is None:
        return f"Error: Product '{name}' not found."

    if quantity <= 0:
        return "Error: Quantity to add must be greater than zero."

    product["stock"] += quantity
    return f"Success: Added {quantity} units to '{product['name']}'. New stock: {product['stock']}."



def sell_product(inventory, name, quantity):
   
    product = search_product(inventory, name)
    if product is None:
        return f"Error: Product '{name}' not found."

    if quantity <= 0:
        return "Error: Sale quantity must be greater than zero."

    if quantity > product["stock"]:
        return f"Error: Insufficient stock. Available: {product['stock']}, Requested: {quantity}."

    product["stock"] -= quantity
    return f"Success: Sold {quantity} units of '{product['name']}'. Remaining stock: {product['stock']}."


def calculate_total_inventory_value(inventory):
    
    total = sum(item["price"] * item["stock"] for item in inventory)
    return round(total, 2)


def get_low_stock_report(inventory, threshold=5):
    
    low_stock_items = [item for item in inventory if item["stock"] < threshold]
    return low_stock_items