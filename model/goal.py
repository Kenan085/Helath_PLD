from database import db  # Import the database module
from models.user import User  # Import User model

class Goal(db.Model):
    """Represents a health goal for a user."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    goal_type = db.Column(db.String(50), nullable=False)  # e.g., "water", "sleep", "exercise"
    target_value = db.Column(db.Float, nullable=False)  # Target value for the goal
    start_date = db.Column(db.Date, nullable=False)  # Start date of the goal
    end_date = db.Column(db.Date, nullable=False)  # End date of the goal
    # Add any other goal-related fields (e.g., progress, status)

    user = db.relationship('User', backref=db.backref('goals', lazy=True))  # Relation to User

    def __repr__(self):
        return f'<Goal {self.goal_type}: {self.target_value} for user {self.user_id}>'