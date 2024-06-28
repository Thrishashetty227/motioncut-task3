import json
import os
from datetime import datetime

# Constants
DATA_FILE = 'expenses.json'

# Load expenses from file
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save expenses to file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file)

# Add a new expense
def add_expense(expenses):
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., food, transportation): ")
        description = input("Enter description: ")
        
        if date not in expenses:
            expenses[date] = []
        
        expenses[date].append({
            'amount': amount,
            'category': category,
            'description': description
        })
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter the correct data.")

# View expenses
def view_expenses(expenses):
    for date, expense_list in expenses.items():
        print(f"\nDate: {date}")
        for expense in expense_list:
            print(f"  Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

# Analyze expenses
def analyze_expenses(expenses):
    category_totals = {}
    monthly_totals = {}
    
    for date, expense_list in expenses.items():
        month = date[:7]  # YYYY-MM
        for expense in expense_list:
            category = expense['category']
            amount = expense['amount']
            
            if category not in category_totals:
                category_totals[category] = 0
            category_totals[category] += amount
            
            if month not in monthly_totals:
                monthly_totals[month] = 0
            monthly_totals[month] += amount
    
    print("\nCategory-wise Expenditure:")
    for category, total in category_totals.items():
        print(f"  {category}: {total}")
    
    print("\nMonthly Expenditure:")
    for month, total in monthly_totals.items():
        print(f"  {month}: {total}")

# Main function
def main():
    expenses = load_expenses()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            analyze_expenses(expenses)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == '__main__':
    main()