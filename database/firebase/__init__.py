import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import current_app  # To access configuration from app.py

db = None

def init_app(app):
    """Initializes the Firebase database connection."""
    global db

    cred = credentials.Certificate(app.config['FIREBASE_CONFIG'])  # Load credentials from config
    firebase_admin.initialize_app(cred)
    db = firestore.client()  # Connect to Firestore