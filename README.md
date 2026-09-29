# Personal Expense Tracker

## 1. Project Overview

Personal Expense Tracker is a beginner-level, menu-driven Python program for recording and reviewing personal expenses. Users can enter an expense and view simple spending summaries through the command line.

Expense records are kept in the program’s memory while it is running. They are cleared when the program exits.

## 2. Project Objectives

- Practise Python functions, lists, dictionaries, loops, and conditional statements
- Accept and process expense details entered by the user
- Calculate total spending and summarize spending by category
- Organize the program into separate Python modules

## 3. Features

- Add an expense with a date, category, description, and amount
- View expenses entered during the current run
- Calculate the total of the entered expenses
- Display spending grouped by category
- Search for expenses by category
- Handle an invalid menu choice
- Handle an amount that cannot be converted to a number

## 4. Functional Modules

### Main Menu

`main.py` displays the menu, gets the user’s choice, and calls the relevant functions.

### Expense Management

`expense_manager.py` contains the functions for adding, displaying, and searching expenses. The expense records are held in a Python list while the program is running.

### Reports

`report_manager.py` calculates the total spending and the category-wise summary.

### Amount Input

`validation.py` converts the entered amount to a number. If the input is not numeric, the program displays an error message.

## 5. Technologies and Python Concepts

- Python 3
- Functions and modules
- Lists and dictionaries
- Loops and conditional statements
- User input and formatted output
- Basic error handling with `try` and `except`

No additional Python packages are required.

## 6. Project Structure

```text
expense-tracker-project/
├── docs/
│   └── design.md
├── main.py
├── expense_manager.py
├── report_manager.py
├── validation.py
├── README.md
└── statement.md
```

## Design Diagrams

The diagrams are in [docs/design.md](docs/design.md):

- System Architecture Diagram
- Workflow Diagram
- Use-Case Diagram
- Sequence Diagram
- Component Diagram

An ER diagram is not applicable because this project does not use a database or save expense records.

## 7. How to Run the Project

### Requirements

Install Python 3 on your computer.

### Run on macOS or Linux

1. Open Terminal.
2. Change to the project folder.
3. Run:

   ```bash
   python3 main.py
   ```

### Run on Windows

1. Open Command Prompt or PowerShell.
2. Change to the project folder.
3. Run:

   ```bash
   py main.py
   ```

The program menu will appear in the terminal.

## 8. How to Use the Program

Choose a menu number and follow the prompts:

1. Add an expense by entering its date, category, description, and amount.
2. View the expenses entered during the current run.
3. Display the total amount spent.
4. Display spending grouped by category.
5. Search for expenses in a category.
6. Exit the program.

## 9. Manual Testing

The program can be checked manually:

- Add two expenses and confirm they appear under **View All Expenses**.
- Confirm **Show Total Expenses** adds the amounts correctly.
- Confirm **Category Summary** groups amounts by category.
- Search for a category that exists and one that does not.
- Enter an invalid menu choice and confirm the program displays an error.
- Enter a non-numeric amount and confirm the program displays an error.

## 10. Limitations

- Expenses are stored only in memory and are cleared when the program exits.
- The program does not currently update or delete expenses.
- The date is requested in `DD-MM-YYYY` format but is not checked for validity.
- The category names shown in the prompt are suggestions; other category names can be entered.
- The program does not include budgets or save records to a CSV file or database.