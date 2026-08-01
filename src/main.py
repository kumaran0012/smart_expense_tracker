from fastapi import FastAPI, Query, HTTPException
from typing import Optional

from src.models import Expense
from src.storage import load_expenses, save_expenses

app = FastAPI(
    title="Smart Expense Tracker API",
    version="1.0.0"
)

expenses = load_expenses()


@app.get("/")
def home():
    return {"message": "Welcome to Smart Expense Tracker API"}


# Add Expense
@app.post("/expenses")
def add_expense(expense: Expense):

    for exp in expenses:
        if exp["id"] == expense.id:
            raise HTTPException(
                status_code=400,
                detail="Expense ID already exists"
            )

    expenses.append(expense.model_dump(mode="json"))

    save_expenses(expenses)

    return {
        "message": "Expense added successfully",
        "expense": expense
    }


# View All / Filter
@app.get("/expenses")
def get_expenses(category: Optional[str] = Query(default=None)):

    if category is None:
        return expenses

    filtered = []

    for expense in expenses:

        if expense["category"].lower() == category.lower():
            filtered.append(expense)

    return filtered


# Total Expenses
@app.get("/expenses/total")
def get_total(category: Optional[str] = Query(default=None)):

    total = 0

    if category is None:

        for expense in expenses:
            total += expense["amount"]

        return {"total": total}

    for expense in expenses:

        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    return {
        "category": category,
        "total": total
    }


# Delete Expense
@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    for expense in expenses:

        if expense["id"] == expense_id:

            expenses.remove(expense)

            save_expenses(expenses)

            return {
                "message": "Expense deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )