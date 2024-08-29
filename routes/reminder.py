from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.reminder import Reminder
from database import db

reminder_bp = Blueprint('reminder', __name__, template_folder='templates/reminder')

@reminder_bp.route('/manage_reminders', methods=['GET', 'POST'])
@login_required
def manage_reminders():
    if request.method == 'POST':
        # Get data from the form
        reminder_type = request.form['reminder_type']
        description = request.form['description']
        reminder_time = request.form['reminder_time']
        # Add data validation here 
        new_reminder = Reminder(
            user_id=current_user.id,
            reminder_type=reminder_type,
            description=description,
            reminder_time=reminder_time
        )
        try:
            db.session.add(new_reminder)
            db.session.commit()
            flash('Reminder saved successfully!', 'success')
            return redirect(url_for('reminder.manage_reminders'))
        except Exception as e:
            flash('An error occurred. Please try again.', 'error')
            print(f"Error during reminder creation: {e}")
    reminders = Reminder.query.filter_by(user_id=current_user.id).all()
    return render_template('manage_reminders.html', reminders=reminders)