from datetime import date, datetime
from Register_IE import app
from flask import render_template, request, redirect, url_for, flash
from Register_IE.forms import MovementsForm
from Register_IE.models import select_all, insert, select_by, delete_by, update_by

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
        return render_template("new.html", dataForm = form, pageTitle="Admission")

    else:
        if form.validate_on_submit():
            
            insert([form.date.data.isoformat(),
                    form.concept.data,
                    form.quantity.data])
            
            flash('Movement registered')
            return redirect(url_for('index'))     
        else:
            return render_template("new.html", dataForm = form)

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

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    formUpdate = MovementsForm()
    if request.method == "GET":

        result = select_by(id)

        formUpdate.date.data = datetime.strptime(result[1], "%Y-%m-%d")
        formUpdate.concept.data = result[2] 
        formUpdate.quantity.data = result[3]

        return render_template("update.html", dataForm = formUpdate, id = result[0], pageTitle="Modification")
    else:
        if formUpdate.validate_on_submit():
            
            update_by(id, [formUpdate.date.data.isoformat(),
                    formUpdate.concept.data,
                    formUpdate.quantity.data])
            
            flash('Movement updated')
            return redirect(url_for('index'))  

        else:
            return render_template("update.html", dataForm = formUpdate, id = id)

@app.route("/delete/<int:id>", methods=["GET", "POST"])
def remove(id):
    if request.method =="GET":
        result = select_by(id)
        return render_template("delete.html", data=result, pageTitle="Delete") 

    else:
        delete_by(id)
        flash('Movement deleted')
        return redirect(url_for('index'))