from app import db
from .basetable import BaseTable

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
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    contact_number = db.Column(db.String(32))
    client = db.relationship('Client', back_populates='elders')
    documents = db.relationship('Document', back_populates='elder', lazy=True)

    def __repr__(self):
        return '<Elder {}>'.format(self.full_name)
