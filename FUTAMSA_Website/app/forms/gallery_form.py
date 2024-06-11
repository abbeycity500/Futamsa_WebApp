from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class GalleryForm(FlaskForm):
    image = FileField('Image', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    description = StringField('Description')
    submit = SubmitField('Upload')
