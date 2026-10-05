name = input("Name: ")
weight_kg=float(input("Weight in KG: "))
height_m = float(input("Height in meters: "))

BMI = weight_kg/(height_m*height_m)

print("="*50)
print(f"{'BMI REPORT':^50}")
print("="*50)
print(" "*50)
print(f"Name: {name}")
print(f"Weight: {weight_kg}kg")
print(f"Height: {height_m}m")
print(" "*50)

print(f"BMI: {BMI: .2f}")
print("="*50)