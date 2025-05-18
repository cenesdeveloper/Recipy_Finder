import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback_dev_key')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')

