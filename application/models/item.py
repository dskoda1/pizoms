import datetime
from index import db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'), nullable=False)
    size_id = db.Column(db.Integer(), db.ForeignKey('size.id'), nullable=False)
    price = db.Column(db.Float())
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    created_by = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self, *args, **kwargs):
        db.Model.__init__(self, *args, **kwargs)
        self.created_at = datetime.datetime.utcnow()

    def attr(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'size_id': self.size_id,
            'price': self.price,
            'name': self.name,
            'description': self.description,
            'created_by': self.created_by,
            'created_at': self.created_at
        }
