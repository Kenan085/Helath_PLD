from database import db  # Import the database module
from models.user import User  # Import User model

class HealthData(db.Model):
    """Represents health data for a user."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)  # Record the date of the data entry
    # Health metrics
    water_intake = db.Column(db.Float, nullable=False)
    sleep_duration = db.Column(db.Float, nullable=False)
    exercise_duration = db.Column(db.Float, nullable=False)
    calories_consumed = db.Column(db.Integer, nullable=False)
    # Add more custom metrics as needed (e.g., weight, heart rate, steps)

    user = db.relationship('User', backref=db.backref('health_data', lazy=True))  # Relation to User

    def __repr__(self):
        return f'<HealthData for user {self.user_id} on {self.date}>'