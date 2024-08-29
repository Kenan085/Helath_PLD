from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.goal import Goal
from database import db

goal_bp = Blueprint('goal', __name__, template_folder='templates/goal')

@goal_bp.route('/set_goals', methods=['GET', 'POST'])
@login_required
def set_goals():
    if request.method == 'POST':
        # Get data from the form
        goal_type = request.form['goal_type']
        target_value = request.form['target_value']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        # Add data validation here 
        new_goal = Goal(
            user_id=current_user.id,
            goal_type=goal_type,
            target_value=target_value,
            start_date=start_date,
            end_date=end_date
        )
        try:
            db.session.add(new_goal)
            db.session.commit()
            flash('Goal saved successfully!', 'success')
            return redirect(url_for('goal.set_goals'))
        except Exception as e:
            flash('An error occurred. Please try again.', 'error')
            print(f"Error during goal creation: {e}")
    return render_template('set_goals.html')

@goal_bp.route('/view_goals')
@login_required
def view_goals():
    goals = Goal.query.filter_by(user_id=current_user.id).all()
    return render_template('view_goals.html', goals=goals)