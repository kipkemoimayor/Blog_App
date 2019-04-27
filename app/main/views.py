from . import main
from flask import render_template
from .forms import CommentForm,AdminBlog
from .. import db



@main.route("/")
def index():
    title="Blog"
    message="Welcome to my Blog"
    form = CommentForm()
    return render_template("index.html",message=message,title=title,comments=form)

@main.route("/new_blog")
def new_blog():
    form=AdminBlog()
    title="Write a blog"
    return render_template("new_blog.html",title=title,newBlog=form)
