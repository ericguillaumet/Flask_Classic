from Register_IE import app
from flask import render_template
from Register_IE.models import select_all

@app.route("/")
def index():

    registers = select_all()

    movement_data=[
        {"id": 1, "date": "2023-01-01", "concept":"Salary", "quantity": 1500},
        {"id": 2, "date": "2023-01-05", "concept":"Cake", "quantity": -10},
        {"id": 3, "date": "2023-01-06", "concept":"Clothes", "quantity": -40},
    ]
    return render_template("index.html", pageTitle="All", data=registers)