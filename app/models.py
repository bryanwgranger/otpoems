from flask import current_app
from app import db

class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.Integer)
    poet = db.Column(db.String(120))
    poem = db.Column(db.String(255))
    total_tokens = db.Column(db.Integer)
