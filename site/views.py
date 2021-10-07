from flask import Blueprint, json, render_template, request, jsonify, redirect, url_for


frontpage = Blueprint(__name__, "frontpage")

name = "allen"

@frontpage.route("/")
def home():
    return render_template("index.html", name=name)

@frontpage.route("/profile")
def profile(username):
    args = request.args
    name = args.get("name")
    return render_template("index.html", name=username)

@frontpage.route("/json")
def get_json():
    return jsonify({})

@frontpage.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@frontpage.route("/backhome")
def backhome():
    return redirect(url_for("views.home"))