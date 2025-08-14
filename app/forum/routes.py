# app/forum/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..models import ForumCategory, ForumPost, ForumComment, User
from .. import db

forum_bp = Blueprint('forum', __name__, url_prefix='/forum')

@forum_bp.route('/')
def categories():
    categories = ForumCategory.query.all()
    return render_template('forum/categories.html', title='Forum', categories=categories)

@forum_bp.route('/category/<int:category_id>')
def category(category_id):
    category = ForumCategory.query.get_or_404(category_id)
    posts = ForumPost.query.filter_by(category_id=category_id).order_by(ForumPost.timestamp.desc()).all()
    return render_template('forum/category.html', title=category.name, category=category, posts=posts)

@forum_bp.route('/post/<int:post_id>')
def post(post_id):
    post = ForumPost.query.get_or_404(post_id)
    comments = ForumComment.query.filter_by(post_id=post_id).order_by(ForumComment.timestamp.asc()).all()
    return render_template('forum/post.html', title=post.title, post=post, comments=comments)

@forum_bp.route('/new_post/<int:category_id>', methods=['GET', 'POST'])
@login_required
def new_post(category_id):
    category = ForumCategory.query.get_or_404(category_id)
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        if title and body:
            post = ForumPost(title=title, body=body, user_id=current_user.id, category_id=category_id)
            db.session.add(post)
            db.session.commit()
            flash('Your post has been created!', 'success')
            return redirect(url_for('forum.post', post_id=post.id))
    return render_template('forum/new_post.html', title='New Post', category=category)

@forum_bp.route('/new_comment/<int:post_id>', methods=['POST'])
@login_required
def new_comment(post_id):
    post = ForumPost.query.get_or_404(post_id)
    body = request.form.get('body')
    if body:
        comment = ForumComment(body=body, user_id=current_user.id, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted!', 'success')
    return redirect(url_for('forum.post', post_id=post_id))

