from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, RadioField, SelectField, TextField, TextAreaField, \
    SubmitField

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'


class InfoForm(FlaskForm):
    name = StringField('What is your name', validators=[DataRequired()])
    morethan = BooleanField(">18?")
    mood = RadioField('Please choose your mood:', choices=[('mood_one', 'happy'), ('mood_two', "excited")])
    food_choice = SelectField(u'Pick your favourite food:',
                              choices=[('ch', 'Chicken'), ('bf', 'Beef'), ('fsh', "Fish")])
    feedback = TextAreaField()
    submit = SubmitField('submit')


@app.route('/', methods=["GET", "POST"])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['morethan'] = form.morethan.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thankyou'))
    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
