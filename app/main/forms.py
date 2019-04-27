from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo

class CommentForm(FlaskForm):
    email=StringField('Your email ',validators=[Required(),Email()])
    name=StringField("Your name",validators=[Required()])
    comment=TextAreaField("Comment",validators=[Required()])
    submit=SubmitField("Submit")

class AdminBlog(FlaskForm):

    title=StringField("Your name",validators=[Required()])
    body=TextAreaField("Comment",validators=[Required()])
    submit=SubmitField("Submit")
