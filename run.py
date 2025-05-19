import os

from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        if not User.query.filter_by(username='demo').first():
            demo_user = User(
                username='demo',
                password=generate_password_hash('demo123')
            )
            db.session.add(demo_user)
            db.session.commit()

    if os.environ.get("FLASK_ENV") != "production":
        app.run(debug=True)
