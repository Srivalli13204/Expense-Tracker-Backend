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

## Authentication

![login-browser](https://github.com/user-attachments/assets/6b1f0b81-3e14-4d20-8d90-243f851b5dd6)


### Login - Get JWT Token

POST /api/login/

Request:

```bash
{
  "email": "your_email@example.com",
  "password": "your_password"
}
```

Response:

```bash
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

Use this token in the Authorization header for all other requests:

```bash
Authorization: Bearer <access_token>
```

## API Endpoints

| Method | Endpoint                   | Description                    |
| ------ | -------------------------- | ------------------------------ |
| POST   | `/api/login/`              | Obtain JWT tokens              |
| POST   | `/api/expenses/`           | Create a new expense           |
| GET    | `/api/expenses/list/`      | Get all expenses (filterable)  |
| GET    | `/api/expenses/analytics/` | Get total + category analytics |


## Filter Expenses by Date

Example:

![api-login](https://github.com/user-attachments/assets/e222fca3-d5ea-4147-b7ad-2bfbabf2e9a4)

![api-expenses](https://github.com/user-attachments/assets/f9c96974-d88d-4c13-a021-cd945c681f08)

![api-expenses-list](https://github.com/user-attachments/assets/cfb9e637-f1f4-4030-9f88-ab276e20f079)

![api-expenses-analytics](https://github.com/user-attachments/assets/c63531ed-9fa4-4cf0-86af-70e0de03e421)

## Author
Pichika Parimala Durga Srivalli
isiri1320@gmail.com
