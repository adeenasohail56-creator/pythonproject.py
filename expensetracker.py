expenses = []

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    expense = {
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\n--- All Expenses ---")

        for expense in expenses:
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("--------------------")


def show_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expenses:", total)


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")

