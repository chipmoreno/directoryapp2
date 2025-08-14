# app/events/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from ..models import Event, User
from .. import db
from datetime import datetime

events_bp = Blueprint('events', __name__, url_prefix='/events')

@events_bp.route('/')
def calendar():
    return render_template('events/calendar.html', title='Event Calendar')

@events_bp.route('/data')
def data():
    events = Event.query.all()
    return jsonify([{
        'title': event.title,
        'start': event.start_time.isoformat(),
        'end': event.end_time.isoformat(),
        'url': url_for('events.event', event_id=event.id)
    } for event in events])

@events_bp.route('/<int:event_id>')
def event(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('events/event.html', title=event.title, event=event)

@events_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_event():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        location = request.form.get('location')
        if title and description and start_time and end_time:
            event = Event(
                title=title, 
                description=description, 
                start_time=datetime.fromisoformat(start_time), 
                end_time=datetime.fromisoformat(end_time), 
                location=location, 
                user_id=current_user.id
            )
            db.session.add(event)
            db.session.commit()
            flash('Your event has been created!', 'success')
            return redirect(url_for('events.calendar'))
    return render_template('events/new_event.html', title='New Event')
