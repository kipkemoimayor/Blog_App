from . import main
from flask import render_template,redirect,url_for,flash,request,abort
from .forms import CommentForm,AdminBlog,DeleteBlog,DeleteComment
from .. import db
import markdown2
from ..models import Blogs,Comments,Users
from ..request import get_quote
from ..email import mail_message



@main.route("/")
def index():
    quote=get_quote()
    title="Blog"
    message="Welcome to my Blog"
    blogs=Blogs.query.all()
    form = CommentForm()
    return render_template("index.html",quote=quote,message=message,title=title,comments=form,blogs=blogs)

@main.route("/new_blog",methods=["POST","GET"])
def new_blog():
    #query all emails
    emails=Comments.query.all()
    all_emails=[]
    for emal in emails:
        all_emails.append(emal.email)


    form=AdminBlog()
    if form.validate_on_submit():
        blog=Blogs(title=form.title.data,body=form.body.data)
        db.session.add(blog)
        db.session.commit()
        mail_message("Hello A new Blog has been posted","email/welcome_user","")
        return redirect(url_for('main.index'))

    title="Write a blog"
    return render_template("new_blog.html",title=title,newBlog=form,all_emails=all_emails)

@main.route("/read_blog/title/<int:id>/",methods=['GET','POST'])
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
        # flash("Blog deleted sucessfully","success")
        return redirect(url_for('main.index'))
    # del_comment=DeleteComment()
    # if del_comment.validate_on_submit():
    #     dele_com=Comments.query.filter_by(blog_id=id).all()
    #     db.session.delete(dele_com)
    #     db.session.commit()
    #
    #     return redirect(url_for('main.read_blog',id=blog_id))



    return render_template("read_blog.html",deleform=del_form,data=data,blogComment=blog_comment,format_blog=format_blog,message=message,title=title,comments=form,blogs=blogs,id=id)

#profile pic
@main.rout("/profile/<uname>")
def profile(uname):
    user=Users.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html")
