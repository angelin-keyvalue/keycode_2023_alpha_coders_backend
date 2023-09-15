from app import db
from .basetable import BaseTable
from werkzeug.security import generate_password_hash

class Buddy(BaseTable):
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    gender = db.Column(db.String(1))
    phone_number = db.Column(db.String(128))
    address = db.Column(db.Text)
    age = db.Column(db.Integer)
    city = db.Column(db.String(128))

        
    def __repr__(self):
        return '<Buddy {}>'.format(self.name)
