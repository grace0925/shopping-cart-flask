from flask import render_template, request, redirect, make_response, url_for, flash
from flask import current_app as app
from .models import db, Item


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        req = request.form

        name = req["name"]
        quantity = req["quantity"]
        units = req["unit"]

        unit_string = handle_unit(int(units))
        print('name: ', name, ' quantity: ', quantity, ' unit: ', unit_string)

        new_item = Item(name, quantity, unit_string)
        db.session.add(new_item)
        db.session.commit()

        flash("Successfully created and stored new item!")

        return redirect(url_for('home'))
    return render_template("index.html")


def handle_unit(units):
    switcher = {
        1: 'kg',
        2: "g",
        3: "mg",
        4: "L",
        5: "mL",
        6: "unit",
        7: "bag"
    }
    return switcher.get(units, "Invalid unit")
