from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'somekey'


class SimpleForm(FlaskForm):
    name = StringField('What is your name', validators=[DataRequired()], render_kw={"placeholder": "name"})
    submit = SubmitField('Click me')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        flash('Yo, {} click the button tho'.format(session['name']))
        return redirect(url_for('index'))

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
