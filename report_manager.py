def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print("\n--- Total Expenses ---")
    print(f"Total amount spent: ₹{total:.2f}")


def category_summary(expenses):
    print("\n--- Category Summary ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]

        if category in summary:
            summary[category] += expense["amount"]
        else:
            summary[category] = expense["amount"]

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")