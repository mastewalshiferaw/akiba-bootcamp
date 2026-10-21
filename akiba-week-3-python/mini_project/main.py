from products import add_product, display_all_products, find_product, update_product_info
from sales import record_sale
from reports import display_reports


def get_positive_float(prompt):
    
    while True:
        try:
            val = float(input(prompt))
            if val >= 0:
                return val
            print("Value cannot be negative. Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_positive_int(prompt):
    
    while True:
        try:
            val = int(input(prompt))
            if val >= 0:
                return val
            print("Value cannot be negative. Try again.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def main():
    
    products = [
        {"id": "P01", "name": "Cooking Oil", "price": 4.50, "stock": 15},
        {"id": "P02", "name": "Sugar 1kg", "price": 1.80, "stock": 4},
        {"id": "P03", "name": "Wheat Flour", "price": 2.20, "stock": 20},
        {"id": "P04", "name": "Mineral Water", "price": 0.75, "stock": 3}
    ]
    sales = []

    while True:
        print("\n===== AKIBA BUSINESS TOOLKIT =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Record Sale")
        print("6. View Reports")
        print("7. Exit")
        print("==================================")

        choice = input("Enter your choice (1-7): ").strip()

     
        if choice == "1":
            print("\n--- Add New Product ---")
            p_id = input("Enter Product ID: ").strip()
            if find_product(products, p_id) is not None:
                print("Error: A product with this ID already exists.")
                continue

            name = input("Enter Product Name: ").strip()
            if len(name) == 0:
                print("Error: Product name cannot be empty.")
                continue

            price = get_positive_float("Enter Price: ")
            stock = get_positive_int("Enter Stock Quantity: ")

            add_product(products, p_id, name, price, stock)
            print(f"Product '{name}' added successfully!")


        elif choice == "2":
            display_all_products(products)


        elif choice == "3":
            print("\n--- Search Product ---")
            query = input("Enter Product ID or Name to search: ").strip()
            product = find_product(products, query)

            if product is not None:
                print("\nProduct Details:")
                print(f"  ID    : {product['id']}")
                print(f"  Name  : {product['name']}")
                print(f"  Price : ${product['price']:.2f}")
                print(f"  Stock : {product['stock']}")
            else:
                print("Product not found.")


        elif choice == "4":
            print("\n--- Update Product ---")
            query = input("Enter Product ID or Name to update: ").strip()
            product = find_product(products, query)

            if product is None:
                print("Error: Product not found.")
                continue

            print(f"Editing '{product['name']}' (Current Price: ${product['price']:.2f}, Stock: {product['stock']})")
            print("1. Update Price")
            print("2. Update Stock")
            print("3. Update Both")
            print("4. Cancel")
            sub_choice = input("Choose an option: ").strip()

            if sub_choice == "1":
                new_price = get_positive_float("Enter new price: ")
                update_product_info(product, new_price=new_price)
                print("Price updated successfully!")
            elif sub_choice == "2":
                new_stock = get_positive_int("Enter new stock quantity: ")
                update_product_info(product, new_stock=new_stock)
                print("Stock updated successfully!")
            elif sub_choice == "3":
                new_price = get_positive_float("Enter new price: ")
                new_stock = get_positive_int("Enter new stock quantity: ")
                update_product_info(product, new_price=new_price, new_stock=new_stock)
                print("Product updated successfully!")
            elif sub_choice == "4":
                print("Update cancelled.")
            else:
                print("Invalid choice.")


        elif choice == "5":
            print("\n--- Record Sale ---")
            query = input("Enter Product ID or Name sold: ").strip()
            product = find_product(products, query)

            if product is None:
                print("Error: Product not found.")
                continue

            print(f"Selected: {product['name']} | Stock: {product['stock']} | Unit Price: ${product['price']:.2f}")
            quantity = get_positive_int("Enter quantity to sell: ")

            success, result = record_sale(products, sales, query, quantity)

            if success:
                print("Sale recorded successfully!")
                print(f"Sale Total     : ${result:.2f}")
                print(f"Remaining Stock: {product['stock']}")
            else:
                print(result)

     
        elif choice == "6":
            display_reports(products, sales, low_stock_threshold=5)

        elif choice == "7":
            print("\nThank you for using Akiba Business Toolkit. Goodbye!")
            break

        else:
            print("Invalid option! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()