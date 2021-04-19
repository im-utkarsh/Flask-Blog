from flask import current_app as app

from flaskblog import db

with app.app_context():
    db.create_all()
