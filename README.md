# Expense Tracker

This is a Django web application for managing expenses.

## Getting Started

Follow these steps to run the app on your local machine:

### Prerequisites

- Python 
- Django 
- Matplotlib

### Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/yashsindhu04/expenseproject.git
   ```

2. Change to the project directory:

   ```shell
   cd expenseproject
   ```

3. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```shell
   python manage.py migrate
   ```

5. Run the development server:

   ```shell
   python manage.py runserver
   ```

### Accessing the Application

Once the development server is running, you can access the main page of the application at the following URL:

```
http://localhost:8000/expense_tracker/expenses
```

You can now log in with the superuser account you created earlier to start managing your expenses.

## Usage

User can add, edit and delete expenses as well as view a breakdown of expenses by category.
