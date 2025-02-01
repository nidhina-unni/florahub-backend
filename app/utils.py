from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password):
    """Hashes a plaintext password."""
    return generate_password_hash(password)


def verify_password(hashed_password, password):
    """Verifies a hashed password against a plaintext password."""
    return check_password_hash(hashed_password, password)
