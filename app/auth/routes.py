# app/auth/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, RegistrationForm
from ..models import User
from .. import db

# Create a Blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # If user is already logged in, redirect them
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))

    form = RegistrationForm()
    if form.validate_on_submit():
        # Use the set_password method from your User model
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('register.html', title='Register', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # If user is already logged in, redirect them
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))

    form = LoginForm()
    if form.validate_on_submit():
        # <<< CHANGED: Query by username to match your form >>>
        user = User.query.filter_by(username=form.username.data).first()
        
        # Use your custom check_password method
        if user and user.check_password(password=form.password.data):
            login_user(user)
            # Redirect to the user's profile page after login
            return redirect(url_for('main.profile'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
            
    return render_template('login.html', title='Login', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

@auth_bp.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    # This is a placeholder. You'll need a form for changing passwords later.
    flash("Change Password page is under construction!", 'info')
    return render_template('auth/change_password.html', title='Change Password') # You'd need to create this template