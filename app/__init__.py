from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['SECRET_KEY'] = 'a_very_secret_key_that_you_should_change'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/auth_app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Import models here to ensure they are registered with SQLAlchemy
        from . import models

        # Register Blueprints
        from app.users.routes import users_bp
        app.register_blueprint(users_bp)    
        from .auth.routes import auth_bp
        app.register_blueprint(auth_bp)
        from .main.routes import main_bp
        app.register_blueprint(main_bp)
        from app.subscriptions.routes import subscriptions_bp
        app.register_blueprint(subscriptions_bp)
        from app.listings.routes import listings_bp
        app.register_blueprint(listings_bp)
        from app.events.routes import events_bp
        app.register_blueprint(events_bp)
        from app.forum.routes import forum_bp
        app.register_blueprint(forum_bp)
        from app.messages.routes import messages_bp
        app.register_blueprint(messages_bp)

        # IMPORTANT: populate_db() should NOT be called here.
        # It should be run as a separate script or Flask CLI command
        # after the application and database are fully set up.

        # --- CUSTOM ERROR HANDLERS START ---
        @app.errorhandler(404)
        def not_found_error(error):
            return render_template('errors/404.html'), 404

        @app.errorhandler(403)
        def forbidden_error(error):
            return render_template('errors/403.html'), 403
        # --- CUSTOM ERROR HANDLERS END ---

        return app
