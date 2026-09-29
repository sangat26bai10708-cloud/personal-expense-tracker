from expense_manager import (
    expenses,
    add_expense,
    view_expenses,
    search_category
)
from report_manager import total_expenses, category_summary


def main():
    while True:
        print("\n==============================")
        print("   PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Expenses")
        print("4. Category Summary")
        print("5. Search by Category")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            search_category()
        elif choice == "6":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()