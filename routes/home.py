from flask import Blueprint, render_template

homeRoute = Blueprint('home', __name__)

@homeRoute.route("/")
def main_page():
    return render_template('index.html')