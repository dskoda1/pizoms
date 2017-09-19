from datetime import datetime

from index import db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.active = True
        self.password = User.hashed_password(password)
        self.created_at = datetime.utcnow()

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password)

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None
