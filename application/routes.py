from flask import render_template, request, redirect, make_response, url_for, flash
from flask import current_app as app
from .models import db, Item


@app.route("/", methods=['GET'])
def home():
    items = Item.query.all()
    return render_template("index.html", items=items)


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


@app.route('/edit', methods=['GET', 'POST'])
def edit_item():
    if request.method == 'POST':
        req = request.form

        name = req["name"]
        quantity = req["quantity"]
        units = req["unit"]
        item_id = int(req["id"])

        unit_string = handle_unit(int(units))
        print('id: ', item_id, 'name: ', name, ' quantity: ', quantity, ' unit: ', unit_string)

        item = Item.query.get(item_id)
        item.item_name = name
        item.item_quantity = quantity
        item.item_unit = unit_string

        db.session.commit()
        flash("Successfully updated item #")

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
