# Import necessary libraries from Flask
from flask import Flask, redirect, request, render_template, url_for
from forms import TransactionForm
from datetime import datetime

# Instantiate Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Sample data representing transactions
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: Route to list all transactions
@app.route("/transactions")
def get_transactions():
    balance = sum(transaction['amount'] for transaction in transactions)
    return render_template("transactions.html", transactions=transactions, balance=balance)

# Create operation: Route to display and process add transaction form
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        # Extract form data to create a new transaction object
        transaction = {
            'id': len(transactions) + 1,         # Generate a new ID based on the current length of the transactions list
            'date': form.date.data,        # Get the 'date' field value from the form
            'amount': float(form.amount.data) # Get the 'amount' field value from the form and convert it to a float
        }

        # Append the new transaction to the transactions list
        transactions.append(transaction)

        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for("get_transactions"))

    # Render the form template to display the add transaction form if the request method is GET
    return render_template("form.html", form=form)

# Update operation: Route to display and process edit transaction form
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    form = TransactionForm()
    transaction = next((t for t in transactions if t['id'] == transaction_id), None)
    if not transaction:
        return "Transaction not found", 404

    if form.validate_on_submit():
        transaction['date'] = form.date.data
        transaction['amount'] = float(form.amount.data)
        return redirect(url_for("get_transactions"))

    form.date.data = datetime.strptime(transaction['date'], '%Y-%m-%d')
    form.amount.data = transaction['amount']
    return render_template("edit.html", form=form, transaction=transaction)

# Delete operation: Route to delete a transaction
@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete_transaction(transaction_id):
    global transactions
    transactions = [t for t in transactions if t['id'] != transaction_id]
    return redirect(url_for("get_transactions"))

@app.route("/search", methods=["GET", "POST"])
def search_transactions():
    if request.method == "POST":
        min_amount = float(request.form['min_amount'])
        max_amount = float(request.form['max_amount'])

        filtered_transactions = [transaction for transaction in transactions if min_amount <= transaction['amount'] <= max_amount]

        return render_template("transactions.html", transactions=filtered_transactions, balance=sum(t['amount'] for t in filtered_transactions))

    return render_template("search.html")

@app.route("/balance")
def total_balance():
    balance = sum(transaction['amount'] for transaction in transactions)
    return f"Total Balance: {balance}"

@app.route("/")
def index():
    return redirect(url_for('get_transactions'))

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)