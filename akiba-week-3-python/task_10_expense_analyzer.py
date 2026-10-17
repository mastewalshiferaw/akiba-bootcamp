
expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 120},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]


def add_expense(expenses, description, category, amount):
    expense = {
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def spending_by_category(expenses):
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    return categories


def largest_expense(expenses):
    if len(expenses) == 0:
        return None

    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    return largest


def expenses_above_threshold(expenses, threshold):
    result = []

    for expense in expenses:
        if expense["amount"] > threshold:
            result.append(expense)

    return result


def category_percentages(expenses):
    total = calculate_total(expenses)
    categories = spending_by_category(expenses)
    percentages = {}

    if total == 0:
        return percentages

    for category in categories:
        percentages[category] = categories[category] / total * 100

    return percentages


def highest_spending_category(expenses):
    categories = spending_by_category(expenses)

    if len(categories) == 0:
        return None

    highest = max(categories, key=categories.get)

    return highest, categories[highest]


def generate_report(expenses, threshold=200):
    print("\n--- Spending Report ---")

    print("Total expenses:", calculate_total(expenses))

    print("\nSpending by category:")
    categories = spending_by_category(expenses)
    percentages = category_percentages(expenses)

    for category in categories:
        print(
            f"{category}: {categories[category]} "
            f"({percentages[category]:.2f}%)"
        )

    largest = largest_expense(expenses)

    if largest is not None:
        print("\nLargest expense:", largest["description"])
        print("Amount:", largest["amount"])

    highest = highest_spending_category(expenses)

    if highest is not None:
        print("\nHighest spending category:", highest[0])
        print("Category total:", highest[1])

    print(f"\nExpenses above {threshold}:")

    above_threshold = expenses_above_threshold(expenses, threshold)

    if len(above_threshold) == 0:
        print("No expenses found.")
    else:
        for expense in above_threshold:
            print(
                expense["description"],
                "-",
                expense["amount"]
            )



add_expense(expenses, "Coffee", "Food", 80)


generate_report(expenses, 200)
