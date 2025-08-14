# app/data.py

from .models import Category, Role
from . import db

def populate_db():
    # Populate Roles
    roles = ['user', 'admin']
    for role_name in roles:
        if not Role.query.filter_by(name=role_name).first():
            role = Role(name=role_name)
            db.session.add(role)

    # Populate Categories
    categories = ['Real Estate', 'For Sale', 'Services', 'Jobs']
    for category_name in categories:
        if not Category.query.filter_by(name=category_name).first():
            category = Category(name=category_name)
            db.session.add(category)

    db.session.commit()