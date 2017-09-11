from index import db

class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(400), nullable=True)
    created_by = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)

    def attr(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_by': self.created_by
        }
