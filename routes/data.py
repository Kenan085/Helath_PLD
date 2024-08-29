from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from models.health_data import HealthData
from database import db

data_bp = Blueprint('data', __name__, template_folder='templates/data')

@data_bp.route('/data_entry', methods=['GET', 'POST'])
@login_required
def data_entry():
    if request.method == 'POST':
        # Get data from the form
        water_intake = request.form['water_intake']
        sleep_duration = request.form['sleep_duration']
        exercise_duration = request.form['exercise_duration']
        calories_consumed = request.form['calories_consumed']
        # Add data validation here 
        new_data = HealthData(
            user_id=current_user.id,
            date=datetime.datetime.now().date(),  # Record the current date
            water_intake=water_intake,
            sleep_duration=sleep_duration,
            exercise_duration=exercise_duration,
            calories_consumed=calories_consumed
        )
        try:
            db.session.add(new_data)
            db.session.commit()
            flash('Data saved successfully!', 'success')
            return redirect(url_for('data.data_entry'))
        except Exception as e:
            flash('An error occurred. Please try again.', 'error')
            print(f"Error during data entry: {e}")
    return render_template('data_entry.html')

@data_bp.route('/get_data')
@login_required
def get_data():
    # Retrieve user's health data
    user_data = HealthData.query.filter_by(user_id=current_user.id).all()
    # Convert data to a format suitable for the frontend (e.g., JSON)
    data_list = [
        {
            'date': item.date.strftime('%Y-%m-%d'),  # Format date for display
            'water_intake': item.water_intake,
            'sleep_duration': item.sleep_duration,
            'exercise_duration': item.exercise_duration,
            'calories_consumed': item.calories_consumed
        } for item in user_data
    ]
    return jsonify(data_list)