from app import create_app, db
from app.data import populate_db

app = create_app()

with app.app_context():
    populate_db()