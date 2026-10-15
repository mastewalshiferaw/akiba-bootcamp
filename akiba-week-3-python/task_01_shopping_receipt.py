items=[ {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]
def calculate_subtotal(items):
    subtotal=0

    for item in items:
        price=item.get("price" )
        quantity= item.get("quantity")

        if price <0:
            raise ValueError(
                f"your price can't be negative")
        if quantity <0:
                raise ValueError(
                    f"Invalid quantity")
        subtotal += price*quantity

    return subtotal



def calculate_discount(subtotal):
     if subtotal>=3000:
          return subtotal*0.1
     elif subtotal>=1000:
          return subtotal*0.05
     else:
          return 0
def calculate_tax(amount, tax_rate):
     if tax_rate<0:
          
          print("INVALID TAX RATE")
     
     tax=(amount * tax_rate)/100

     return tax

def calculate_tax(amount, tax_rate=15):
    """Calculates tax for a given amount and tax percentage."""
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    return (amount * tax_rate) / 100


def generate_receipt(items, tax_rate=15):
   
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    discounted_amount = subtotal - discount
    tax = calculate_tax(discounted_amount, tax_rate)
    final_total = discounted_amount + tax

    receipt_lines = [
        "=" * 40,
        f"{'SHOPPING RECEIPT':^40}",
        "=" * 40,
        f"{'Item':<18}{'Qty':<6}{'Price':<8}{'Total':<8}",
        "-" * 40,
    ]

    for item in items:
        name = item.get("name", "Unknown")
        qty = item.get("quantity", 0)
        price = item.get("price", 0)
        total = price * qty
        receipt_lines.append(f"{name:<18}{qty:<6}{price:<8.2f}{total:<8.2f}")

    receipt_lines.extend([
        "-" * 40,
        f"{'Subtotal:':<28} {subtotal:>10.2f} Birr",
        f"{'Discount:':<28} -{discount:>9.2f} Birr",
        f"{'Tax (' + str(tax_rate) + '%):':<28} {tax:>10.2f} Birr",
        "=" * 40,
        f"{'FINAL TOTAL:':<28} {final_total:>10.2f} Birr",
        "=" * 40,
    ])

    return "\n".join(receipt_lines)


    









