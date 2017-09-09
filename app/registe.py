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

class RegisteForm(Form):
    username = StringField('Username',validators=[DataRequired(),Length(min=6,max=20)])
    password = PasswordField('Password',validators=[
        DataRequired(),
        Length(min=6,max=20),
        EqualTo('confirm',message='Passwords must match!')])
    confirm = PasswordField('Repeat Password')
    workid = StringField('WorkID(IGS)',validators=[DataRequired(),Length(min=6,max=6)])
    email = StringField('Email',validators = [Email()])
    phone = StringField('CelPhone',validators=[DataRequired(),Length(min=11,max=11)])
    section = SelectField('Section(TIH)',choices=[
                  ('ssd','SSD'),
                  ('csv','CSV'),
                  ('swv','SWV'),
                  ('psd','PSD'),
                  ('scd','SCD'),
                  ('syd','SYD')])
    gender = RadioField('Gender',choices=[('m','Male'),('f','Female')],
                 validators=[DataRequired()])
    user_image = SelectField('User_PIC',choices=img_choices)
    submit = SubmitField('Submit')
