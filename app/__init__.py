# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_jwt_extended import JWTManager
#
#
#
# # Initialize SQLAlchemy and Migrate instances (do not bind them to the app here)
# db = SQLAlchemy()
# migrate = Migrate()
# jwt = JWTManager()
#
#
# def create_app():
#     app = Flask(__name__)
#
#     # App configuration
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:db%408910@localhost:5432/postgres'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#     #  JWT
#     app.config['JWT_SECRET_KEY'] = '51099106138700ed2b255d6bae860a4f93bf7e2614bc02c89f28facce8b7a3f6'  # Replace with a strong secret key
#     app.config['JWT_ALGORITHM'] = 'HS256'
#
#     # app.config['JWT_TOKEN_LOCATION'] = ['headers']  # JWT tokens will be expected in headers
#     # app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # Optional: Set token expiry time in seconds (1 hour here)
#     #
#     # # Optional: Set JWT_HEADER_NAME explicitly if different from 'Authorization'
#     # app.config['JWT_HEADER_NAME'] = 'Authorization'  # Default is 'Authorization'
#     #
#     # # Optional: Set JWT_HEADER_TYPE explicitly if you want to change 'Bearer'
#     # app.config['JWT_HEADER_TYPE'] = 'Bearer'  # Default is 'Bearer'
#
#     # Initialize extensions
#     db.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)
#
#     # Import and register blueprints inside the function to avoid circular imports
#     from app.routes.users import user_bp
#     from app.routes.products import products_bp
#     from app.routes.pre_booking import pre_bookings_bp
#     from app.routes.orders import orders_bp
#     from app.routes.admin import admins_bp
#
#     # Register blueprints
#     app.register_blueprint(user_bp, url_prefix='/api')
#     app.register_blueprint(products_bp, url_prefix='/api')
#     app.register_blueprint(pre_bookings_bp, url_prefix='/api')
#     app.register_blueprint(orders_bp, url_prefix='/api')
#     app.register_blueprint(admins_bp, url_prefix='/api')
#
#     return app
#

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

    # JWT configuration
    # # Load JWT_SECRET_KEY from an environment variable or generate it once
    # jwt_secret = os.getenv('JWT_SECRET_KEY')  # Attempt to read the secret from the environment
    # if not jwt_secret:
    #     jwt_secret = secrets.token_hex(32)  # Generate a secure key if not provided
    #     print(f"Generated a new JWT_SECRET_KEY: {jwt_secret}")

    # app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY') or secrets.token_hex(32)
    # app.config['JWT_ALGORITHM'] = 'HS256'
    # app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # Optional: Set token expiry time in seconds (1 hour)
    app.config['JWT_SECRET_KEY'] = '7c4b8a9e3201c5f382747a7dba3f1e9c5e6a2d497f4f6a7b8329b76c95dfe634'  # Replace with an environment variable in production

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
