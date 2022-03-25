from flask import Blueprint, render_template

msg = Blueprint("msg", __name__)


@msg.route("/")
def home():
    return render_template("home.html")

@msg.route("/messages")
def messages():
    return render_template("messages.html")