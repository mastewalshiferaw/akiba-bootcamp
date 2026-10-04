employee_name = input("Employee Name: ")
basic_salary = float(input("Basic Salary: "))
transport_allowance = float(input("Transport allowance: "))
food_allowance = float(input("Food Allowance: "))

gross_salary = basic_salary + transport_allowance + food_allowance

print("="*50)
print(f"{'EMPLOYEE PAYSLIP':^50}")
print("="*50)
print(f"Employee: {employee_name}")
print(f"Basic Salary: {basic_salary}ETB")
print(f"Transport Allowance: {transport_allowance}ETB")
print(f"Food Allowance: {food_allowance}ETB")
print("-"*40)
print(f"Gross Salary: {gross_salary}ETB")
print("="*50)