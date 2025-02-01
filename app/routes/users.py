# from flask import Blueprint, request, jsonify
# from werkzeug.security import generate_password_hash
# from run import db
#
# from app.models import User
#
# user_bp = Blueprint('user_bp', __name__)
#
#
# @user_bp.route('/register', methods=['POST'])
# def user_register():
#     """
#     User registration endpoint. Accepts user details and creates a new user.
#     """
#     data = request.get_json()
#
#     # Validation: Ensure required fields are provided
#     if not all(data.get(field) for field in ['username', 'password', 'email', 'phone', 'address']):
#         return jsonify({"message": "All fields are required"}), 400
#
#     # Check if username or email exists
#     if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
#         return jsonify({"message": "Username or email already exists"}), 409
#
#     # Hash the password
#     hashed_password = generate_password_hash(data['password'])
#
#     # Assign seller_id if is_seller is True
#     seller_id = None
#     if data.get('is_seller'):
#         # Generate the next seller_id (incremental value)
#         max_seller_id = db.session.query(db.func.max(User.seller_id)).scalar()
#         seller_id = (max_seller_id or 0) + 1
#
#     # Create the new user
#     new_user = User(
#         username=data['username'],
#         password=hashed_password,
#         email=data['email'],
#         phone=data['phone'],
#         address=data['address'],
#         is_seller=data.get('is_seller', False),
#         seller_id=seller_id  # Include seller_id if the user is a seller
#     )
#
#     try:
#         db.session.add(new_user)
#         db.session.commit()
#         return jsonify({"message": "User registered successfully", "user_id": new_user.user_id}), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"message": "An error occurred", "details": str(e)}), 500

# ------------------------------------------------------------------------------------------------


from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.models import User
from app import db  # Directly import the db instance

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def user_register():
    data = request.get_json()

    # Validate input
    if not all(data.get(field) for field in ['username', 'password', 'email', 'phone', 'address']):
        return jsonify({"message": "All fields are required"}), 400

    # Check for existing user
    if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Username or email already exists"}), 409

    # Create new user
    hashed_password = generate_password_hash(data['password'])
    new_user = User(
        username=data['username'],
        password=hashed_password,
        email=data['email'],
        phone=data['phone'],
        address=data['address'],
        is_seller=data.get('is_seller', False)
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201
