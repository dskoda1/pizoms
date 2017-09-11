from index import db

class Size(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    size = db.Column(db.String(100), unique=True)

    def attr(self):
        return {
            'id': self.id,
            'size': self.size,
        }
