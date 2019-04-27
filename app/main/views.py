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
    blogs=Blogs.query.all()
    form = CommentForm()
    return render_template("index.html",message=message,title=title,comments=form,blogs=blogs)

@main.route("/new_blog",methods=["POST","GET"])
def new_blog():
    form=AdminBlog()
    if form.validate_on_submit():
        blog=Blogs(title=form.title.data,body=form.body.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))

    title="Write a blog"
    return render_template("new_blog.html",title=title,newBlog=form)

@main.route("/read_blog/title/<int:id>")
def read_blog(id):
    title="Blog"
    message="Welcome to my Blog"
    blogs=Blogs.query.all()
    form = CommentForm()


    format_blog=markdown2.markdown(blogs[id-1].body,extras=["code-friendly", "fenced-code-blocks"])
    return render_template("read_blog.html",format_blog=format_blog,message=message,title=title,comments=form,blogs=blogs,id=id)
