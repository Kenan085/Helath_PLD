from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.user import User
from models.health_data import HealthData
from database import db

user_bp = Blueprint('user', __name__, template_folder='templates/user')

@user_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@user_bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        # Update user data (e.g., username, email, etc.)
        # Add data validation here 
        current_user.username = request.form['username']
        current_user.email = request.form['email']
        # ... update other fields 
        try:
            db.session.commit()
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('user.profile'))
        except Exception as e:
            flash('An error occurred. Please try again.', 'error')
            print(f"Error during profile update: {e}")
    return render_template('edit_profile.html', user=current_user)