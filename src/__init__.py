from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    
    # Configure SQLite database
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///brand_guide.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    
    with app.app_context():
        # Import routes and models here to avoid circular imports
        from .routes import brand_guide_bp, pdf_bp
        
        # Register blueprints
        app.register_blueprint(brand_guide_bp)
        app.register_blueprint(pdf_bp)
        
        # Create database tables
        db.create_all()
    
    return app