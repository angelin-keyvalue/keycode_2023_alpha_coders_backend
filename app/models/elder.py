from app import db
from .basetable import BaseTable

from werkzeug.security import generate_password_hash, check_password_hash

class Elder(BaseTable):
    full_name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    is_alone = db.Column(db.Boolean, default=False)
    gender = db.Column(db.String(1))
    address = db.Column(db.Text)
    pincode = db.Column(db.Integer)
    landmark = db.Column(db.String(64))
    illness = db.Column(db.Text)
    client_relationship = db.Column(db.String(32))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    contact_number = db.Column(db.Integer)

    
    def __repr__(self):
        return '<Elder {}>'.format(self.full_name)
    
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    
    def check_password(self, password):
        return check_password_hash(self.password, password)
