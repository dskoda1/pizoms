from index import db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    price = db.Column(db.Float())
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'), nullable=False)
    size_id = db.Column(db.Integer(), db.ForeignKey('size.id'), nullable=False)
    created_by = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(100), nullable=True)

    def attr(self):
        return {
            'id': self.id,
            'price': self.name,
            'category_id': self.category_id,
            'size_id': self.size_id,
            'description': self.description,
            'created_by': self.created_by
        }
