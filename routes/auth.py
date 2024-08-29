from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from database import db

auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('user.profile'))  # Redirect to user's profile
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Add password hashing for security
        hashed_password = generate_password_hash(password) 
        new_user = User(username=username, email=email, password_hash=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            # Handle potential database errors
            flash('An error occurred. Please try again.', 'error')
            print(f"Error during signup: {e}")
            return render_template('signup.html')
    return render_template('signup.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('auth.login'))