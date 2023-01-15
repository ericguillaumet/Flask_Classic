from datetime import date
from Register_IE import app
from flask import render_template, request, redirect, url_for
from Register_IE.models import select_all, insert


def validateForm(requestForm):
    today = date.today().isoformat() #isoformat lo transforma en string
    errors =[]
    if requestForm['date'] > today:
        errors.append("Date: the introduced date is not valid")
    if requestForm['concept'] == "":
        errors.append("Empty concept: Introduce a concept for the register")
    if requestForm['quantity'] == "" or float(requestForm['quantity']) == 0.0:
        errors.append("The quantity is empty or equals zero: Introduce a positive or negative quantity")
    return errors

@app.route("/")
def index():
    registers = select_all()

    movement_data=[
        {"id": 1, "date": "2023-01-01", "concept":"Salary", "quantity": 1500},
        {"id": 2, "date": "2023-01-05", "concept":"Cake", "quantity": -10},
        {"id": 3, "date": "2023-01-06", "concept":"Clothes", "quantity": -40},
    ]
    return render_template("index.html", pageTitle="All", data=registers)

@app.route("/new", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new.html", dataForm = None)
    else:
        errors = validateForm(request.form)

        if errors:
            return render_template("new.html", msgError = errors, dataForm = request.form)
        else:
            insert([request.form['date'],
                    request.form['concept'],
                    request.form['quantity']])

            return redirect(url_for('index'))