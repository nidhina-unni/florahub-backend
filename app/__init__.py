import os
import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:db%408910@localhost:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = '7c4b8a9e3201c5f382747a7dba3f1e9c5e6a2d497f4f6a7b8329b76c95dfe634'

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints
    from app.routes.users import user_bp
    from app.routes.products import products_bp
    from app.routes.pre_booking import pre_bookings_bp
    from app.routes.orders import orders_bp
    from app.routes.admin import admins_bp
    from app.routes.cart import cart_bp
    from app.routes.product_feedback import feedback_bp
    from app.routes.website_feedback import website_feedback_bp
    from app.routes.payment import payments_bp

    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(products_bp, url_prefix='/api')
    app.register_blueprint(pre_bookings_bp, url_prefix='/api')
    app.register_blueprint(orders_bp, url_prefix='/api')
    app.register_blueprint(admins_bp, url_prefix='/api')
    app.register_blueprint(cart_bp, url_prefix='/api')
    app.register_blueprint(feedback_bp, url_prefix='/api')
    app.register_blueprint(website_feedback_bp, url_prefix='/api')
    app.register_blueprint(payments_bp, url_prefix='/api')

    return app
