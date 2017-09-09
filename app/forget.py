from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SelectField,RadioField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class ForgetForm(Form):
    username = StringField('Username',validators=[DataRequired(),Length(min=6,max=20)])
    workid = StringField('WorkID(IGS)',validators=[DataRequired(),Length(min=6,max=6)])
    email = StringField('Email',validators = [Email()])
    password = PasswordField('NewPassword',validators=[
        DataRequired(),
        Length(min=6,max=20),
        EqualTo('confirm',message='Passwords must match!')])
    confirm = PasswordField('Repeat Password')
