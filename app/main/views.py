from . import main
from flask import render_template,redirect,url_for,flash,request
from .forms import CommentForm,AdminBlog,DeleteBlog
from .. import db
import markdown2
from ..models import Blogs,Comments



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

@main.route("/read_blog/title/<int:id>",methods=['GET','POST'])
def read_blog(id):
    blog_id=id
    title="Blog"
    message="Welcome to my Blog"
    blog=Blogs.query.filter_by(id=id).first()
    blogs=Blogs.query.all()
    data=blog.title
    form = CommentForm()

    if form.validate_on_submit():
        comments=Comments(blog_id=id,email=form.email.data,username=form.name.data,comment=form.comment.data)
        comments.save_comments()
        return redirect(url_for('main.read_blog',id=blog_id))



    format_blog=markdown2.markdown(blog.body,extras=["code-friendly", "fenced-code-blocks"])

    blog_comment=Comments.query.filter_by(blog_id=id).all()


    del_form=DeleteBlog()
    if del_form.validate_on_submit():
        dele=Blogs.query.filter_by(id=id).first()
        db.session.delete(dele)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template("read_blog.html",deleform=del_form,data=data,blogComment=blog_comment,format_blog=format_blog,message=message,title=title,comments=form,blogs=blogs,id=id)
