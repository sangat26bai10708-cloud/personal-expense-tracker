# Project Design

## 1. System Architecture

```mermaid
flowchart TD
    User[User]
    Main[main.py<br/>Menu and program flow]
    Expense[expense_manager.py<br/>Add, view, search]
    Reports[report_manager.py<br/>Total and category summary]
    Validation[validation.py<br/>Read numeric amount]
    Memory[(In-memory expense list)]

    User --> Main
    Main --> Expense
    Main --> Reports
    Expense --> Validation
    Expense --> Memory
    Reports --> Memory
```

## 2. Workflow Diagram

```mermaid
flowchart TD
    Start([Start]) --> Menu[Display menu]
    Menu --> Choice{User choice}
    Choice -->|1| Add[Enter expense details]
    Add --> Amount[Read amount]
    Amount --> Store[Add expense to in-memory list]
    Store --> Menu
    Choice -->|2| View[Display expenses]
    View --> Menu
    Choice -->|3| Total[Calculate total spending]
    Total --> Menu
    Choice -->|4| Summary[Display category summary]
    Summary --> Menu
    Choice -->|5| Search[Search by category]
    Search --> Menu
    Choice -->|6| Exit([Exit])
```

## 3. Use-Case Diagram

```mermaid
flowchart LR
    User([User])

    subgraph Tracker[Personal Expense Tracker]
        Add([Add expense])
        View([View expenses])
        Total([Show total spending])
        Summary([View category summary])
        Search([Search by category])
    end

    User --- Add
    User --- View
    User --- Total
    User --- Summary
    User --- Search
```

## 4. Sequence Diagram: Adding an Expense

```mermaid
sequenceDiagram
    actor User
    participant Main as main.py
    participant Expense as expense_manager.py
    participant Validation as validation.py
    participant List as In-memory expense list

    User->>Main: Select Add Expense
    Main->>Expense: Call add_expense()
    Expense->>User: Ask for date, category, description
    Expense->>Validation: Request amount
    Validation->>User: Prompt for amount
    User-->>Validation: Enter amount
    Validation-->>Expense: Return number or None
    Expense->>List: Add expense if amount is valid
    Expense-->>User: Show result
```

## 5. Component Diagram

```mermaid
flowchart LR
    Main[main.py]
    Expense[expense_manager.py]
    Reports[report_manager.py]
    Validation[validation.py]

    Main --> Expense
    Main --> Reports
    Expense --> Validation
```

## 6. Storage Design

Expenses are stored in memory in a Python list. Each expense is represented by a dictionary containing `date`, `category`, `description`, and `amount`. The records are cleared when the program exits. There is no database, so an ER diagram is not applicable.