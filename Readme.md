# Smart Expense Tracker API

## Features

- Add Expense
- View All Expenses
- Filter by Category
- Calculate Total Expenses
- Delete Expense

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn src.main:app --reload
```

Swagger:

```
http://127.0.0.1:8000/docs
```

## Tests

```bash
pytest
```