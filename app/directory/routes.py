# app/directory/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..models import Business, Review, User
from .. import db

directory_bp = Blueprint('directory', __name__, url_prefix='/directory')

@directory_bp.route('/')
def businesses():
    businesses = Business.query.all()
    return render_template('directory/businesses.html', title='Business Directory', businesses=businesses)

@directory_bp.route('/business/<int:business_id>')
def business(business_id):
    business = Business.query.get_or_404(business_id)
    reviews = Review.query.filter_by(business_id=business_id).order_by(Review.timestamp.desc()).all()
    return render_template('directory/business.html', title=business.name, business=business, reviews=reviews)

@directory_bp.route('/new_business', methods=['GET', 'POST'])
@login_required
def new_business():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        category = request.form.get('category')
        address = request.form.get('address')
        phone = request.form.get('phone')
        website = request.form.get('website')
        if name and description and category:
            business = Business(name=name, description=description, category=category, address=address, phone=phone, website=website, user_id=current_user.id)
            db.session.add(business)
            db.session.commit()
            flash('Your business has been listed!', 'success')
            return redirect(url_for('directory.business', business_id=business.id))
    return render_template('directory/new_business.html', title='New Business')

@directory_bp.route('/new_review/<int:business_id>', methods=['POST'])
@login_required
def new_review(business_id):
    business = Business.query.get_or_404(business_id)
    rating = request.form.get('rating')
    comment = request.form.get('comment')
    if rating and comment:
        review = Review(rating=rating, comment=comment, user_id=current_user.id, business_id=business_id)
        db.session.add(review)
        db.session.commit()
        flash('Your review has been posted!', 'success')
    return redirect(url_for('directory.business', business_id=business_id))