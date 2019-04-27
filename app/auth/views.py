from flask import render_template,redirect,url_for
from . import auth
from .forms import RegisterForm
from .. import db
from ..models import Users


@auth.route("/login")
def login():
    return render_template("auth/login.html")

@auth.route("/register",methods=['POST',"GET"])
def register():
    title="Registration"
    form=RegisterForm()
    if form.validate_on_submit():
        user=Users(email=form.data.email,username=form.data.username,pass_secure=form.data.password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for(".login"))


    return render_template("auth/register.html",registration=form)
