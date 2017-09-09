from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,IntegerField
from wtforms.validators import DataRequired,Length

class LoginForm(Form):
    username = StringField('Username',validators=[DataRequired(),Length(min=6)])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=6)])

class JumpNotice(Form):
    page_num = IntegerField(validators=[DataRequired()])
