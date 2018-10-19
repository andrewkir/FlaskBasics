from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField("Name of Puppy: ")
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):
    id = IntegerField("Id Number of Puppy to remove")
    submit = SubmitField('Delete Puppy')


class AddOwnerForm(FlaskForm):
    owner_name = StringField("Name of Owner: ")
    puppy_id = IntegerField('Puppy id:')
    submit = SubmitField('Add owner')