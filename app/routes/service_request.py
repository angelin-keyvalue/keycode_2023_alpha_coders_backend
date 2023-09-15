from app.routes import bp
from app.models.service_request import ServiceRequest
from app.schema.service_request import ServiceRequestSchema
from flask import request,jsonify
from datetime import datetime
from flask_cors import cross_origin

from app import db

@bp.route('/service/request', methods=['POST'])
@cross_origin(origin='*')
def create_service_request():
    body = request.get_json()
    service_request = ServiceRequest(service_name=body['service_name'],
                                     date_time_of_service=datetime.strptime(body['date_time_of_service'],'%Y-%m-%d %H:%M:%S'),
    pickup_location = body['pickup_location'],
    pickup_latitude = body['pickup_latitude'],
    pickup_longitude = body['pickup_longitude'],
    gender_preference = body['gender_preference'],
    recurring_event = body['recurring_event'],
    recurring_freq =  body['recurring_freq'],
    wheelchair_assistance = body['wheelchair_assistance'],
    transportation = body['transportation'],
    status = body['status'],
    elder_id = body['elder_id'],
    client_id = body['client_id'],
    # buddy_id = body['buddy_id'],
    hospital_name =  body['hospital_name'],
    doctor_name =  body['doctor_name'],
    appointment_time = datetime.strptime(body['appointment_time'],'%Y-%m-%d %H:%M:%S'))
    db.session.add(service_request)
    db.session.commit()
    
    return {"id":str(service_request.id),"status_code":"200"}

@bp.route('/service/request', methods=['GET'])
@cross_origin(origin='*')
def get_service_requests():
    services_schema = ServiceRequestSchema(many=True)
    all_budies = ServiceRequest.query.all()
    return jsonify(services_schema.dump(all_budies))

@bp.route('/service/<int:id>/request', methods=['PUT'])
@cross_origin(origin='*')
def update_request_status(id):
    body = request.get_json()
    service = db.session.execute(db.select(ServiceRequest).filter_by(id=id)).scalar_one()
    service.status = body['status']
    db.session.commit()
    return {"id":str(service.id),"status_code":"200"}