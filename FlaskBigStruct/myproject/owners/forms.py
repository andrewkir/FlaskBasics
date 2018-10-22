from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddOwnerForm(FlaskForm):
    owner_name = StringField("Name of Owner: ")
    puppy_id = IntegerField('Puppy id:')
    submit = SubmitField('Add owner')