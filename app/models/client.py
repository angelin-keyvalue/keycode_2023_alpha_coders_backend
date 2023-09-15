from app import db
from .basetable import BaseTable

from werkzeug.security import generate_password_hash, check_password_hash

class Client(BaseTable):
    full_name = db.Column(db.String(64))
    contact_number = db.Column(db.Integer)
    address = db.Column(db.Text)
    email = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))

    
    def __repr__(self):
        return '<Client {}>'.format(self.email)
    
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    
    def check_password(self, password):
        return check_password_hash(self.password, password)
