import os
from flask import Flask
#from app.models import db
import secrets

def create_app(test_config=None):
    # Create and Configure the Application
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load instance config, if exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config, if passed
        app.config.from_mapping(test_config)

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    app.config['SECRET_KEY'] = secrets.token_hex(16)

    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    """

    # Register Blue Prints
    from .routes import main
    app.register_blueprint(main)

    """
    # Create Database Tables
    with app.app_context():
        db.create_all()
    """

    return app
