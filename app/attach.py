from flask_wtf import Form
from flask_wtf.file import FileField,FileAllowed,FileRequired

class AttachForm(Form):
    
    attach = FileField('Choose your attachment: ',validators=[FileRequired(),FileAllowed(['jpg','png','gif'],'Images Only!')])
