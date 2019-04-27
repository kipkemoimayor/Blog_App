from . import main
from flask import render_template
from .forms import CommentForm
from .. import db


@main.route("/")
def index():
    title="Blog"
    message="Welcome to my Blog"
    form = CommentForm()
    return render_template("index.html",message=message,title=title,comments=form)
