usd=float(input("USD Amount: "))

exchange_rate = float(input("Enter exchange rate($1=?ETB): "))
etb=usd*exchange_rate

print("="*50)
print(f"{'CURRENCY EXCHANGE':^50}")
print("="*50)
print(""*50)
print(f"USD Amount: {usd}")
print(f"Exchange Rate: 1 USD = {exchange_rate} ETB")
print(f"ETB Amount: {etb}ETB")
print("="*50)