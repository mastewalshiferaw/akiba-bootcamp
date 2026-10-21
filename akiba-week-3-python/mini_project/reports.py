
def calculate_total_revenue(sales):

    total_revenue = 0.0
    for sale in sales:
        total_revenue += sale["total"]
    return total_revenue


def calculate_inventory_value(products):
  
    total_value = 0.0
    for product in products:
        total_value += product["price"] * product["stock"]
    return total_value


def get_low_stock_products(products, threshold=5):
    
    low_stock = []
    for product in products:
        if product["stock"] <= threshold:
            low_stock.append(product)
    return low_stock


def display_sales_summary(sales):
   
    if len(sales) == 0:
        print("No sales recorded yet.")
        return

    print(f"{'Product':<18} {'Qty':<6} {'Unit Price':<12} {'Total':<10}")
    print("-" * 48)
    for s in sales:
        print(f"{s['product_name']:<18} {s['quantity']:<6} ${s['unit_price']:<11.2f} ${s['total']:<9.2f}")


def display_reports(products, sales, low_stock_threshold=5):
  
    print("\n" + "=" * 50)
    print("             BUSINESS REPORT SUMMARY")
    print("=" * 50)

    #Total Revenue
    revenue = calculate_total_revenue(sales)
    print(f"Total Sales Revenue        : ${revenue:.2f}")

    #Total Inventory Value
    inv_value = calculate_inventory_value(products)
    print(f"Total Inventory Asset Value: ${inv_value:.2f}")

    # Low-Stock Alert
    print(f"\nLow Stock Products (<= {low_stock_threshold} units):")
    low_stock = get_low_stock_products(products, low_stock_threshold)
    if len(low_stock) == 0:
        print("  All products are adequately stocked.")
    else:
        for p in low_stock:
            print(f"  - {p['name']} (ID: {p['id']}) -> {p['stock']} units left")

    #Summary
    print("\nSales Transactions History:")
    display_sales_summary(sales)
    print("=" * 50)