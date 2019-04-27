from . import main
from flask import render_template

@main.route("/")
def index():
    title="Blog"
    message="Welcome to my Blog"
    return render_template("index.html",message=message,title=title)
