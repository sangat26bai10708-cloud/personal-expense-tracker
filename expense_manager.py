from validation import get_amount

expenses = []


def add_expense():
    print("\n--- Add Expense ---")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Shopping/Bills/Other): ")
    description = input("Enter description: ")

    amount = get_amount()
    if amount is None:
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("-" * 70)
    print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>10}")
    print("-" * 70)

    for expense in expenses:
        print(
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<25}"
            f"₹{expense['amount']:>9.2f}"
        )

    print("-" * 70)


def search_category():
    print("\n--- Search by Category ---")
    category = input("Enter category to search: ")
    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(
                f"Date: {expense['date']} | "
                f"Description: {expense['description']} | "
                f"Amount: ₹{expense['amount']:.2f}"
            )
            found = True

    if not found:
        print("No expenses found in this category.")