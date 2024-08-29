from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy

db = SQLAlchemy()  # Initialize SQLAlchemy instance

from .user import User  # Import User model
from .health_data import HealthData  # Import HealthData model
from .goal import Goal  # Import Goal model
from .reminder import Reminder  # Import Reminder model