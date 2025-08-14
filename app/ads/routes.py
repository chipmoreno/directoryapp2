# app/ads/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..models import Ad
from .. import db
from datetime import datetime

ads_bp = Blueprint('ads', __name__, url_prefix='/ads')

@ads_bp.route('/')
@login_required
def manage_ads():
    # Only admin users can manage ads
    if not current_user.has_role('admin'):
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('main.index'))
    ads = Ad.query.all()
    return render_template('ads/manage_ads.html', title='Manage Ads', ads=ads)

@ads_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_ad():
    if not current_user.has_role('admin'):
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        image_url = request.form.get('image_url')
        link_url = request.form.get('link_url')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        if image_url and link_url and start_date and end_date:
            ad = Ad(
                image_url=image_url, 
                link_url=link_url, 
                start_date=datetime.fromisoformat(start_date), 
                end_date=datetime.fromisoformat(end_date)
            )
            db.session.add(ad)
            db.session.commit()
            flash('Ad created successfully!', 'success')
            return redirect(url_for('ads.manage_ads'))
    return render_template('ads/new_ad.html', title='New Ad')

@ads_bp.route('/<int:ad_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_ad(ad_id):
    if not current_user.has_role('admin'):
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('main.index'))
    ad = Ad.query.get_or_404(ad_id)
    if request.method == 'POST':
        ad.image_url = request.form.get('image_url')
        ad.link_url = request.form.get('link_url')
        ad.start_date = datetime.fromisoformat(request.form.get('start_date'))
        ad.end_date = datetime.fromisoformat(request.form.get('end_date'))
        ad.is_active = 'is_active' in request.form
        db.session.commit()
        flash('Ad updated successfully!', 'success')
        return redirect(url_for('ads.manage_ads'))
    return render_template('ads/edit_ad.html', title='Edit Ad', ad=ad)

@ads_bp.route('/<int:ad_id>/delete', methods=['POST'])
@login_required
def delete_ad(ad_id):
    if not current_user.has_role('admin'):
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('main.index'))
    ad = Ad.query.get_or_404(ad_id)
    db.session.delete(ad)
    db.session.commit()
    flash('Ad deleted successfully!', 'success')
    return redirect(url_for('ads.manage_ads'))

# Can you implement the backend stuff on the frontend? for example: ads, directory, forum, messages, subscriptions, 