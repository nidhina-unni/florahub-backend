# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from app.routes.users import user_bp  # Import the user blueprint
#
#
# # Initialize SQLAlchemy instance
# db = SQLAlchemy()
# migrate = Migrate()
#
#
# from urllib.parse import quote
#
# password = "db@8910"
# encoded_password = quote(password)
# print(encoded_password)  # Outputs: db%408910
#
# # def create_app():
# #     app = Flask(__name__)
# #     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/db_name'
# #     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# #
# #     db.init_app(app)
# #     return app
#
#
# def create_app():
#     app = Flask(__name__)
#
#     # Database configuration
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:db%408910@localhost:5432/postgres'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#     # Initialize SQLAlchemy and Flask-Migrate
#     db.init_app(app)
#     migrate.init_app(app, db)
#
#     # Register blueprints
#     app.register_blueprint(user_bp, url_prefix='/api')
#
#     # Create tables in the database if not present
#     with app.app_context():
#         db.create_all()
#
#     return app
#
#
# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)

# --------------------------------------------------------------------------

from app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

