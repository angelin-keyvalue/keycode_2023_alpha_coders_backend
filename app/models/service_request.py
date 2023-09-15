from app import db
from .basetable import BaseTable

class ServiceRequest(BaseTable):
    service_name = db.Column(db.String(128), index=True)
    date_time_of_service = db.Column(db.DateTime)
    pickup_time = db.Column(db.DateTime)
    pickup_location = db.Column(db.String(300))
    pickup_latitude = db.Column(db.String(300))
    pickup_longitude = db.Column(db.String(300))
    gender_preference = db.Column(db.String(1))
    recurring_event = db.Column(db.Boolean)
    recurring_freq =  db.Column(db.String(300))
    wheelchair_assistance = db.Column(db.Boolean)
    transportation = db.Column(db.String(300))
    status = db.Column(db.String(300))
    elder_id = db.Column(db.Integer, db.ForeignKey('elder.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    buddy_id = db.Column(db.Integer, db.ForeignKey('buddy.id'))
    hospital_name =  db.Column(db.String(300))
    doctor_name =  db.Column(db.String(300))
    appointment_time = db.Column(db.DateTime)

    def __repr__(self):
        return '<ServiceRequest {}>'.format(self.service_name)
