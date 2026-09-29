# Project Statement

## 1. Project Title

Personal Expense Tracker

## 2. Problem Statement

Keeping track of everyday expenses can help people understand how much they spend and where their money goes. Calculating totals or comparing spending by category manually can take time.

The Personal Expense Tracker is a simple command-line Python program that lets a user enter expenses and view basic spending summaries.

## 3. Scope of the Project

The project focuses on entering and reviewing expenses through a menu-driven application.

The system allows users to:

- Add an expense with a date, category, description, and amount
- View expenses entered during the current run
- Calculate total spending
- View category-wise spending
- Search for expenses by category

Expenses are kept in memory only. They are cleared when the program exits.

The current project does not include expense editing or deletion, budgets, monthly reports, highest-expense reports, or permanent file or database storage.

## 4. Target Users

The target users of this project are:

- Students learning Python
- Individuals who want to practise recording and reviewing expenses
- Beginner programmers learning to organize a command-line application

## 5. High-Level Features

### Expense Entry

The user can enter an expense’s date, category, description, and amount.

### Expense Viewing

The user can display the expenses entered during the current program run.

### Spending Summary

The program calculates the total of the entered expenses and groups spending by category.

### Category Search

The user can search for expenses by entering a category.

### Input Handling

The program handles non-numeric amount input and invalid menu choices by displaying an error message.

## 6. Objectives

The main objectives of the project are:

- To build a beginner-level command-line application in Python
- To practise functions, modules, lists, dictionaries, loops, and conditional statements
- To record and display expense information during a program run
- To calculate a total and category-wise spending summary
- To organize program features across separate Python files

## 7. Non-Functional Requirements

- **Usability:** The program presents a numbered menu and prompts the user for information.
- **Reliability:** The program handles invalid menu choices and non-numeric amount input with an error message.
- **Maintainability:** The menu, expense functions, reports, and amount input are organized into separate Python files.
- **Portability:** The program uses Python 3 and does not require additional packages.