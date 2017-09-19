import datetime
from index import db

class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(400), nullable=True)
    created_by = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self, *args, **kwargs):
        db.Model.__init__(self, *args, **kwargs)
        self.created_at = datetime.datetime.utcnow()

    def attr(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_by': self.created_by,
            'created_at': self.created_at
        }
