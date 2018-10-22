from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddOwnerForm

owners_blueprint = Blueprint('owners', __name__,
                             template_folder='templates/owners')


@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddOwnerForm()
    if form.validate_on_submit():
        owner_name = form.owner_name.data
        pup_id = form.puppy_id.data
        owner = Owner(owner_name, pup_id)
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add_owner.html', form=form)
