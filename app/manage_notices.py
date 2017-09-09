from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SelectField,RadioField,SubmitField,TextAreaField,IntegerField
from wtforms.validators import DataRequired,Length,EqualTo,Email,NumberRange

class Add_Notices_Form(Form):
    title_add = StringField('Title',validators =[DataRequired(),Length(min=6,max=1024)])
    author = StringField('Author',validators = [DataRequired()])
    content_add = TextAreaField('Content',default="Please input the new's content",validators=[DataRequired(),Length(min=11,max=1024)])
    species_add = SelectField('Type',choices=[
                         ('notice','Notice'),
                         ('news','News'),
                         ('club notice','Club Notice'),
                         ('training','Training')])

class Edit_Notices_Form(Form):
    title_edit = StringField('Title',validators =[DataRequired(),Length(min=6,max=1024)])
    content_edit = TextAreaField('Content',default="Please input the new's content",validators=[DataRequired(),Length(min=11,max=1024)])
    species_edit = SelectField('Type',choices=[
                         ('notice','Notice'),
                         ('news','News'),
                         ('club notice','Club Notice'),
                         ('training','Training')])

class Jump_Notices_Form(Form):
    jump_num = IntegerField(validators=[DataRequired()])

class Button_Add(Form):
    add_button = SubmitField("Add")

class Button_Edit(Form):
    edit_button = SubmitField("Edit")

class Button_Delete(Form):
    delete_button = SubmitField("Delete")

class Button_Check(Form):
    check_button = BooleanField(validators = [DataRequired()],default="")
