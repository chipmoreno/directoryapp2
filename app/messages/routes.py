# app/messages/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..models import Message, User, Listing
from .. import db
from sqlalchemy import or_

messages_bp = Blueprint('messages', __name__, url_prefix='/messages')

@messages_bp.route('/')
@login_required
def conversations():
    conversations = db.session.query(Message.listing_id, User.id, User.username).join(User, or_(Message.sender_id == User.id, Message.recipient_id == User.id)).filter(or_(Message.sender_id == current_user.id, Message.recipient_id == current_user.id)).filter(User.id != current_user.id).distinct().all()
    return render_template('messages/conversations.html', title='Conversations', conversations=conversations)

@messages_bp.route('/conversation/<int:listing_id>/<int:recipient_id>', methods=['GET', 'POST'])
@login_required
def conversation(listing_id, recipient_id):
    listing = Listing.query.get_or_404(listing_id)
    recipient = User.query.get_or_404(recipient_id)
    messages = Message.query.filter(
        Message.listing_id == listing_id,
        or_(
            (Message.sender_id == current_user.id) & (Message.recipient_id == recipient_id),
            (Message.sender_id == recipient_id) & (Message.recipient_id == current_user.id)
        )
    ).order_by(Message.timestamp.asc()).all()
    return render_template('messages/conversation.html', title='Conversation', messages=messages, listing=listing, recipient=recipient)

@messages_bp.route('/send/<int:listing_id>/<int:recipient_id>', methods=['POST'])
@login_required
def send_message(listing_id, recipient_id):
    body = request.form.get('body')
    if body:
        message = Message(
            sender_id=current_user.id,
            recipient_id=recipient_id,
            listing_id=listing_id,
            body=body
        )
        db.session.add(message)
        db.session.commit()
        flash('Your message has been sent!', 'success')
    return redirect(url_for('messages.conversation', listing_id=listing_id, recipient_id=recipient_id))