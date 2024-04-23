#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


def display_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")


# In[3]:


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    amount = input("Enter amount: $")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount! Please enter a valid number.")
        return  # Return statement should be inside the function

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])
    print("Expense added successfully!")


# In[6]:


# Function to view all expenses
def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]}, Description: {row[1]}, Amount: ${row[2]}")
    except FileNotFoundError:
        print("No expenses found.")


# In[7]:


# Main function
def main():
    if not os.path.exists("expenses.csv"):
        with open("expenses.csv", "w") as file:
            pass

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")


# In[8]:


if __name__ == "__main__":
    main()


# In[ ]:




