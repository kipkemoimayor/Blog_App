from . import main
from flask import render_template,redirect,url_for,flash,request
from .forms import CommentForm,AdminBlog
from .. import db
import markdown2
from ..models import Blogs



@main.route("/")
def index():
    title="Blog"
    message="Welcome to my Blog"
    form = CommentForm()
    return render_template("index.html",message=message,title=title,comments=form)

@main.route("/new_blog",methods=["POST"])
def new_blog():
    form=AdminBlog()
    if form.validate_on_submit():
        blog=Blogs(title=form.title.data,body=form.body.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))

    title="Write a blog"
    return render_template("new_blog.html",title=title,newBlog=form)
