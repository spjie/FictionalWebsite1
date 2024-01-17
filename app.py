import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/products')
def products():
    return render_template("products.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/confirmation')
def confirmation():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    fullname = firstname + " " + lastname
    email = request.args.get("email")
    phone = request.args.get("phone")
    address = request.args.get("address")
    apt = request.args.get("apt")
    city = request.args.get("city")
    state = request.args.get("state")
    zip = request.args.get("zip")

    props = {
        "fullname": fullname,
        "email": email,
        "phone": phone,
        "address": address,
        "apt": apt,
        "city": city,
        "state": state,
        "zip": zip
    }
    return render_template("confirmation.html", data=props)

if __name__ == '__main__':
    app.run(debug=True)


