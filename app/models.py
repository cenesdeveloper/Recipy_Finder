from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db, login_manager

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    bookmarks = db.relationship('RecipeBookmark', backref='user', lazy=True)

# Bookmark model
class RecipeBookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.String(100), nullable=False)  # Spoonacular recipe ID
    title = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(300), nullable=False)
    source_url = db.Column(db.String(300), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))