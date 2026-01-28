from flask import Flask, render_template, request, redirect
from models import db, Transaction
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def index():
    transactions = Transaction.query.all()
    total = sum(
        t.amount for t in transactions if t.type == "expense"
    )
    return render_template(
        "index.html",
        transactions=transactions,
        total=total
    )

@app.route("/add", methods=["POST"])
def add():
    transaction = Transaction(
        amount=request.form["amount"],
        category=request.form["category"],
        type=request.form["type"]
    )

    db.session.add(transaction)
    db.session.commit()

    return redirect("/")

with app.app_context():
    db.create_all()
