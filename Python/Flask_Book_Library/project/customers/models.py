from project import db, app
import re

# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, name, city, age):
        if len(name) > 20 or not re.match("^[a-zA-Z]+$", name):
            raise ValueError("invalid customer name")
        self.name = name
        if len(city) > 20 or not re.match("^[a-zA-Z]+$", city):
            raise ValueError("invalid city name")
        self.city = city
        self.age = age

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age})"


with app.app_context():
    db.create_all()
