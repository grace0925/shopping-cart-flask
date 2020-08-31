from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask import request, redirect
app = Flask(__name__)


@app.route("/")
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

        return redirect(request.url)
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


if __name__ == "__main__":
    app.run(debug=True)
