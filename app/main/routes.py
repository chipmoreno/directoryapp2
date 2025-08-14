# app/main/routes.py

from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
from ..models import Listing, User, Category, Role, Ad
from app.listings.forms import ListingForm 
from app import db 
from datetime import datetime 

# Create a Blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/index')
def index():
    """Homepage."""
    # Query for the 5 most recent listings
    recent_listings = Listing.query.order_by(Listing.created_at.desc()).limit(5).all()
    
    # Query for a random active ad
    random_ad = Ad.query.filter(Ad.is_active == True, Ad.start_date <= datetime.utcnow(), Ad.end_date >= datetime.utcnow()).order_by(db.func.random()).first()

    all_listings_url = url_for('listings.all_listings')
    create_listing_url = url_for('listings.new_listing')
    
    return render_template(
        'index.html', 
        title='Welcome',
        listings=recent_listings,  # Pass the listings to the template
        all_listings_url=all_listings_url, 
        create_listing_url=create_listing_url,
        random_ad=random_ad
    )

@main_bp.route('/profile')
@login_required
def profile():
    """User profile page."""
    # current_user is automatically available from Flask-Login
    return render_template('profile.html', title='Your Profile', user=current_user)

@main_bp.route('/create_listing')
def create_listing():
    """Create a new listing."""
    return render_template('listings/create_listing.html', title='Create Listing')

@main_bp.route('/my_listings')
@login_required # Ensure only logged-in users can access
def my_listings():
    # Query listings belonging to the current user, ordered by creation date (newest first)
    # Note: current_user.listings is available because of the 'backref' in Listing model's author relationship
    user_listings = current_user.listings.order_by(Listing.created_at.desc()).all()

    return render_template('my_listings.html', title='My Listings', listings=user_listings)


@main_bp.route('/user/<string:username>')
def user_profile(username):
    return redirect(url_for('users.profile', username=username))