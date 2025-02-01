from flask import jsonify
from app.models import Admin
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
import json


# def authenticate_user(admin_name, admin_password):
#     admin = Admin.query.filter_by(admin_name=admin_name).first()
#     if admin and admin.admin_password(admin_password):
#         return create_access_token(identity={'id': admin.id, 'is_admin': admin.is_admin})
#     return None


def authenticate_user(admin_name, admin_password):
    admin = Admin.query.filter_by(admin_name=admin_name).first()
    if admin and check_password_hash(admin.admin_password, admin_password):
        # Create access token with serialized identity (string format)
        identity = json.dumps({'id': admin.admin_id, 'is_admin': admin.is_admin})
        return create_access_token(identity=identity)
    return None


# def authenticate_user(admin_name, admin_password):
#     admin = Admin.query.filter_by(admin_name=admin_name).first()
#     if admin and check_password_hash(admin.admin_password, admin_password):  # Corrected password check
#         return create_access_token(identity={"id": admin.admin_id, "is_admin": admin.is_admin})
#     return None

