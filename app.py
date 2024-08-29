from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS  # Enable CORS for development
from database import db  # Import database module
from models.user import User
from models.health_data import HealthData
from models.goal import Goal
from models.reminder import Reminder
from routes import auth, user, data, goal, reminder

app = Flask(__name__)
CORS(app)  # Enable CORS for development

# Configure your database (replace with your actual database configuration)
app.config['DATABASE_URL'] = 'your_database_url'  # Replace with your actual database URL
db.init_app(app)

# Register blueprints for different functionalities
app.register_blueprint(auth.auth_bp)
app.register_blueprint(user.user_bp)
app.register_blueprint(data.data_bp)
app.register_blueprint(goal.goal_bp)
app.register_blueprint(reminder.reminder_bp)

@app.route('/')
def index():
    return render_template('index.html')

# Error handling for invalid routes
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)