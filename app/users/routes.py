# app/users/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..models import User, Review
from .. import db
from .forms import EditProfileForm

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    reviews = Review.query.filter_by(seller_id=user.id).order_by(Review.timestamp.desc()).all()
    return render_template('users/profile.html', title=f"{user.username}'s Profile", user=user, reviews=reviews)


@users_bp.route('/new_review/<username>', methods=['POST'])
@login_required
def new_review(username):
    user = User.query.filter_by(username=username).first_or_404()
    rating = request.form.get('rating')
    comment = request.form.get('comment')
    if rating and comment:
        review = Review(rating=rating, comment=comment, user_id=current_user.id, seller_id=user.id)
        db.session.add(review)
        db.session.commit()
        flash('Your review has been posted!', 'success')
    return redirect(url_for('users.profile', username=username))

@users_bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username, current_user.email)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.', 'success')
        return redirect(url_for('users.profile', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.about_me.data = current_user.about_me
    return render_template('users/edit_profile.html', title='Edit Profile', form=form)