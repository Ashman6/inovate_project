from flask import Blueprint, Flask, render_template, redirect, Blueprint

my_view = Blueprint('my_view', __name__)

@my_view.route("/")
def home():
    return render_template("home.html")


@my_view.route("/contact")
def contact():
    return render_template("contact.html")

@my_view.route("/about")
def about():
    return render_template("about.html")

@my_view.route("/futurepage.html")
def futurepage():
    return render_template("futurepage.html")

@my_view.route("/futurepagetwo.html")
def futurepagetwo():
    return render_template("futurepagetwo.html")

@my_view.route("/pkm1")
def pkm1():
    return render_template("pkm1.html")


@my_view.route("/pkm2")
def pkm2():
    return render_template("pkm2.html")

@my_view.route("/pkm3")
def pkm3():
    return render_template("pkm3.html")

@my_view.route("/pkm4")
def pkm4():
    return render_template("pkm4.html")


@my_view.route("/pkm5")
def pkm5():
    return render_template("pkm5.html")

@my_view.route("/pkm6")
def pkm6():
    return render_template("pkm6.html")

@my_view.route("/pkm7")
def pkm7():
    return render_template("pkm7.html")


@my_view.route("/pkm8")
def pkm8():
    return render_template("pkm8.html")

@my_view.route("/pkm9")
def pkm9():
    return render_template("pkm9.html")

@my_view.route("/pkm10")
def pkm10():
    return render_template("pkm10.html")

@my_view.route("/pkm11")
def pkm11():
    return render_template("pkm11.html")

@my_view.route("/pkm12")
def pkm12():
    return render_template("pkm12.html")