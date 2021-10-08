from flask import Blueprint, json, render_template, request, jsonify, redirect, url_for


frontpage = Blueprint(__name__, "frontpage")


@frontpage.route("/")
def home():
    return render_template("index.html")

@frontpage.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("views.user", usr=user))
    else:
        return render_template("login.html")

@frontpage.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@frontpage.route("/backhome")
def backhome():
    return redirect(url_for("views.home"))