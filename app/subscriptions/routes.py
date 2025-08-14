# app/subscriptions/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .. import db
from datetime import datetime, timedelta

subscriptions_bp = Blueprint('subscriptions', __name__, url_prefix='/subscriptions')

@subscriptions_bp.route('/')
@login_required
def plans():
    return render_template('subscriptions/plans.html', title='Subscription Plans')

@subscriptions_bp.route('/purchase/<plan_type>')
@login_required
def purchase(plan_type):
    if plan_type == 'premium':
        current_user.subscription_status = 'premium'
        current_user.subscription_end_date = datetime.utcnow() + timedelta(days=30) # 30-day subscription
        db.session.commit()
        flash('You have successfully subscribed to the premium plan!', 'success')
    else:
        flash('Invalid plan type.', 'danger')
    return redirect(url_for('main.profile'))