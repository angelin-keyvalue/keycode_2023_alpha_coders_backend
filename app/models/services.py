from app import db

class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(64), index=True)
    amount = db.Column(db.String(120), index=True, unique=True)
    

    def __repr__(self):
        return '<Services {}>'.format(self.service_name)
