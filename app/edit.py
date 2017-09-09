from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SelectField,RadioField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email

img_choices = [
    ('Apple.gif','Apple'),
    ('Run.gif','Run'),
    ('Panda.gif','Panda'),
    ('Worker.gif','Worker'),
    ('Happy.gif','Happy'),
    ('Gafield.gif','Gafield')
]

class EditForm(Form):
    password = StringField('Password',validators=[
        DataRequired(),
        Length(min=6,max=20),
        EqualTo('confirm',message='Passwords must match!')])
    confirm = StringField('Repeat Password')
    email = StringField('Email',validators = [Email()])
    phone = StringField('CelPhone',validators=[DataRequired(),Length(min=11,max=11)])
    section = SelectField('Section(TIH)',choices=[
                         ('ssd','SSD'),
                         ('csv','CSV'),
                         ('swv','SWV'),
                         ('psd','PSD'),
                         ('scd','SCD'),
                         ('syd','SYD')])
    user_img = SelectField('User_PIC',choices=img_choices,default=img_choices[3])
    submit = SubmitField("Confirm")
