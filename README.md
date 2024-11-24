# Flask Transactions App

This is a simple Flask application to manage transactions. The application allows users to add, edit, delete, and search transactions. It also displays the total balance of all transactions.

## Features

- Add new transactions
- Edit existing transactions
- Delete transactions
- Search transactions by amount range
- Display total balance of transactions

## Requirements

- Python 3.9+
- Flask

## Installation

1. Clone the repository:
2. GO to http://127.0.0.1:5000

## Routes
/: Redirects to /transactions.

/transactions: Displays the list of transactions and the total balance.

/add: Displays a form to add a new transaction.

/edit/<int:transaction_id>: Displays a form to edit an existing transaction.

/delete/<int:transaction_id>: Deletes a transaction.

/search: Displays a form to search transactions by amount range.

/balance: Displays the total balance of all transactions.

```bash

git clone https://github.com/mustafaangi/flask-transactions-app.git

cd flask-transactions-app

python3 app.py

