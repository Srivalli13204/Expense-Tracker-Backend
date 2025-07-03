# EXPENSE TRACKER BACKEND

A simple Django REST API backend for tracking personal expenses. It supports JWT authentication, expense creation, date-based filtering, and analytics like category-wise totals and overall spending.

---

## Tech Stack

- Python 3
- Django
- Django REST Framework
- Simple JWT for token authentication
- SQLite for local development

---

## Features

- JWT based Authentication (Login)
- Create New Expenses
- Filter Expenses by Date Range
- Get Analytics:
  - Total expenses
  - Category-wise breakdown
 
---

## Setup Instructions

Follow these steps to run the project locally:

### 1. Clone the respository

```bash
git clone https://github.com/Srivalli13204/Expense-Tracker-Backend.git
cd Expense_Tracker
```

### 2. Set up virtual environment

```bash
python -m venv tracker
tracker\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create superuser

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```









