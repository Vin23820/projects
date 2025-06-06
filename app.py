from flask import Flask, render_template, request, redirect
import json
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=["POST"])
def add():
    data = load_data()
    amount = float(request.form["amount"])
    category = request.form["category"]
    type_ = request.form["type"]
    date = request.form["date"] or str(datetime.today().date())
    data.append({"amount": amount, "category": category, "type": type_, "date": date})
    save_data(data)
    return redirect("/report")

@app.route('/report')
def report():
    data = load_data()
    income = sum(x["amount"] for x in data if x["type"] == "income")
    expense = sum(x["amount"] for x in data if x["type"] == "expense")
    return render_template("report.html", income=income, expense=expense, savings=income - expense, transactions=data)

if __name__ == '__main__':
    app.run(debug=True)
