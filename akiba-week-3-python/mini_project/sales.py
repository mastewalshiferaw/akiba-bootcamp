from products import find_product


def calculate_sale_total(unit_price, quantity):
    
    return unit_price * quantity


def record_sale(products, sales, identifier, quantity):
   
    product = find_product(products, identifier)

    if product is None:
        return False, "Error: Product not found."

    if quantity <= 0:
        return False, "Error: Quantity must be greater than zero."

    if quantity > product["stock"]:
        return False, f"Error: Insufficient stock. Only {product['stock']} units available."

    
    product["stock"] -= quantity

 
    sale_total = calculate_sale_total(product["price"], quantity)

    
    transaction = {
        "product_id": product["id"],
        "product_name": product["name"],
        "quantity": quantity,
        "unit_price": product["price"],
        "total": sale_total
    }
    sales.append(transaction)

    return True, sale_total