from utils import load_data, save_data, add_transaction, view_report

data = load_data()

while True:
    print("\n1. Add Transaction\n2. View Report\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        amount = float(input("Amount: "))
        category = input("Category: ")
        type_ = input("Type (income/expense): ").lower()
        date = input("Date (YYYY-MM-DD): ") or None
        add_transaction(data, amount, category, type_, date)
        save_data(data)
    elif choice == '2':
        view_report(data)
    elif choice == '3':
        break
    else:
        print("Invalid choice")
