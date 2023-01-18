from datetime import date
from Register_IE import app
from flask import render_template, request, redirect, url_for
from Register_IE.forms import MovementsForm
from Register_IE.models import select_all, insert, select_by, delete_by

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
    form = MovementsForm()
    if request.method == "GET":
        return render_template("new.html", dataForm = form)

    else:
        if form.validate_on_submit():
            
            insert([form.date.data.isoformat(),
                    form.concept.data,
                    form.quantity.data])

            return redirect(url_for('index'))     
        else:
            return render_template("new.html", msgError = {}, dataForm = form)

    """ 
    WITHOUT WTF FORM
    if request.method == "GET":
        return render_template("new.html", dataForm = {})
    else:
        errors = validateForm(request.form)

        if errors:
            return render_template("new.html", msgError = errors, dataForm = request.form)
        else:
            insert([request.form['date'],
                    request.form['concept'],
                    request.form['quantity']])

            return redirect(url_for('index'))
    """

@app.route("/delete/<int:id>", methods=["GET", "POST"])
def remove(id):
    if request.method =="GET":
        result = select_by(id)
        return render_template("delete.html", data=result) 

    else:
        delete_by(id)
        return redirect(url_for('index'))