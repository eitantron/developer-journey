import json


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            return expenses
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


def show_menu():
    print("\n=== Expense tracker ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Show total spent")
    print("4. Show total by category")
    print("5. Quit")


def add_expense(expenses):
    amount = float(input("Amount: "))
    category = input("Category: ")
    note = input("Note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense saved")


def view_expenses(expenses):
    if expenses == []:
        print("No expenses yet.")
    else:
        for expense in expenses:
            print("\nAmount:", expense["amount"])
            print("Category:", expense["category"])
            print("Note:", expense["note"])


def show_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total spent:", total)


def show_total_by_category(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] = totals[category] + amount
        else:
            totals[category] = amount

    for category in totals:
        print(category, ":", totals[category])


def main():
    expenses = load_expenses()

    while True:
        show_menu()

        choice = input("Pick 1-5: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            show_total_by_category(expenses)

        elif choice == "5":
            save_expenses(expenses)
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()