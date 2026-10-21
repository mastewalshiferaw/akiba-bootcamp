def find_product(products, identifier):
   
    query = identifier.strip().lower()
    for product in products:
        if product["id"].lower() == query or product["name"].lower() == query:
            return product
    return None


def add_product(products, product_id, name, price, stock):

    if find_product(products, product_id) is not None:
        return False 

    new_item = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }
    products.append(new_item)
    return True


def update_product_info(product, new_price=None, new_stock=None):
  
    if new_price is not None:
        product["price"] = new_price
    if new_stock is not None:
        product["stock"] = new_stock


def display_all_products(products):
  
    if len(products) == 0:
        print("\nNo products found in inventory.")
        return

    print("\n" + "-" * 50)
    print(f"{'ID':<8} {'Name':<20} {'Price':<10} {'Stock':<8}")
    print("-" * 50)
    for p in products:
        print(f"{p['id']:<8} {p['name']:<20} ${p['price']:<9.2f} {p['stock']:<8}")
    print("-" * 50)