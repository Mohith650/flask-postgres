from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Numeric

db = SQLAlchemy()

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(Numeric(10, 2), nullable=False)
    category = db.Column(db.String(50))
    type = db.Column(db.String(10), nullable=False)
