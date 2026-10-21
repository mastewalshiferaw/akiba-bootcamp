Question 1: Function Design
Why divide a monolithic function?
-it is functionm in which it performs one task.
-Make inputs and outputs clear.
- Functions can be reused independently.
- Testing and Debugging: Smaller functions are easier to test and fix.
How to divide the program:
- Product: find_product(), add_product(), update_stock()
- Sales: calculate_total(), record_sale()
- Reporting: calculate_revenue(), display_report()

def calculate_total(price, quantity):
    return price * quantity

def update_stock(product, quantity):
    if product["stock"] >= quantity:
        product["stock"] -= quantity
        return True
    return False

def print_receipt(name, quantity, total):
    print(f"Sold {quantity}x {name} for ${total}")

Question 2: Mutable Data and Function Side Effects
1. Why do both outputs contain "Bag"?

Both items and products reference the same list. Using .append() modifies the original list.

2. How do lists behave in functions?

Lists are mutable. Operations like .append(), .pop(), and index assignment can change the original list.

3. In-place modification vs. returning a new list
- In-place: Modifies the original list; memory-efficient but causes side effects.
- New list: Creates a separate list, preserving the original but using extra memory.
4. When is in-place modification useful or problematic?
- Useful: Large datasets or intentional shared state.
- Problematic: Can cause unexpected changes and difficult-to-find bugs.

Example: Avoiding Side Effects:
def add_item(items, item):
    new_items = items.copy()
    new_items.append(item)
    return new_items

products = ["Pen", "Book"]
result = add_item(products, "Bag")

print(products)  # ['Pen', 'Book']
print(result)    # ['Pen', 'Book', 'Bag']