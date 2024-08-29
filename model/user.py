from database import db  # Import the database module

class User(db.Model):
    """Represents a user in the application."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # Store password securely
    # Add any other user-related fields (e.g., profile picture, first name, last name, etc.) 

    def __repr__(self):
        return f'<User {self.username}>'