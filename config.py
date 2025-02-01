import os
import urllib.parse
import secrets

password = "db@8910"
encoded_password = urllib.parse.quote(password)


# Generate a secure random string
secure_key = secrets.token_hex(32)  # Generates a 64-character hexadecimal string
print(secure_key)


class Config:
    SECRET_KEY = "a2f87d0c3e4b2da8e09cd7c6bfc45e76289ea1b648d1c5a3d3e1b3f5e6a7493f"  # Flask secret
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:db%408910@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
