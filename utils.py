import json
from datetime import datetime


def load_data():
    try:
        with open("data.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def add_transaction(data, amount, category, type_, date=None):
    if not date:
        date = str(datetime.today().date())
    data.append({"amount": amount, "category": category, "type": type_, "date": date})
    print("Transaction added.")


def view_report(data):
    income = sum(x["amount"] for x in data if x["type"] == "income")
    expense = sum(x["amount"] for x in data if x["type"] == "expense")
    print(f"Total Income: {income} | Total Expenses: {expense} | Savings: {income - expense}")
