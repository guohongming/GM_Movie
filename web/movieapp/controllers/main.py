__author__ = 'Guo'

from flask import (render_template,
                   current_app,
                   Blueprint,
                   redirect,
                   url_for,
                   request,
                   flash,
                   session)

from movieapp.models.forms import LoginForm, RegisterForm
from movieapp.models.models import User, db_user
from flask_login import login_user, logout_user, current_user, login_required

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='./templates'
)


@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    # print(form.username.data)
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.username.data).first()

        login_user(user, remember=form.remember.data)
        flash("you have been logged in !", category="success")
        # print('success')
        return redirect(url_for('movie.index'))
    # print(form.errors)

    return render_template('login.html', form=form)


@main_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('movie.index'))


@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(form.username.data)
        new_user.set_password(form.password.data)

        db_user.session.add(new_user)
        db_user.session.commit()
        flash("Your user has been created, please login.", category="success")

        return redirect(url_for('.login'))

    return render_template('register.html', form=form)
