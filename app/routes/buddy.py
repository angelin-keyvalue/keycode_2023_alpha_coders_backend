from app.routes import bp
from app.models.buddy import Buddy
from werkzeug.security import generate_password_hash,check_password_hash
from flask import request,jsonify,send_file
from flask_cors import cross_origin
from app.schema.buddy import BuddySchema
from app.models.service_request import ServiceRequest
from app.schema.service_request import ServiceRequestSchema
from app import db
import os,app

@bp.route('/buddy', methods=['POST'])
@cross_origin(origin='*')
def create_buddy():
    body = request.get_json()
    
    buddy = Buddy(name = body['name'], email=body['email'], password=generate_password_hash(body['password']),gender=body['gender'],phone_number=body['phone_number'],
                  address=body['address'],age=body['age'],city=body['city'])
    db.session.add(buddy)
    db.session.commit()
    return {"id":str(buddy.id),"status_code":"200"}

@bp.route('/buddy/login', methods=['POST'])
@cross_origin(origin='*')
def login_buddy():
    body = request.get_json()
    buddy = db.session.execute(db.select(Buddy).filter_by(email=body['email'])).scalar_one()
    print(buddy)
    if check_password_hash(buddy.password,body['password']) is False:
        return {"msg":"Unauthorized access","status_code":"401"}
    else:
        return {"id":str(buddy.id),"msg":"Login successful","status_code":"200"}
    

@bp.route('/buddy/<int:id>', methods=['GET'])
@cross_origin(origin='*')
def get_buddy_by_id(id):
    buddies_schema = BuddySchema()
    buddy = db.get_or_404(Buddy, id)
    return buddies_schema.jsonify(buddy)
    
@bp.route('/buddy', methods=['GET'])
@cross_origin(origin='*')
def get_buddy():
    buddies_schema = BuddySchema(many=True)
    all_budies = Buddy.query.all()
    return jsonify(buddies_schema.dump(all_budies))

@bp.route('/buddy/<int:id>/upload', methods=['POST'])
@cross_origin(origin='*')
def upload_buddy_image(id):
    if 'file' not in request.files:
            return {'message': 'No file part'}, 400

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return {'message': 'No selected file'}, 400
    file_path = os.path.join('app/buddy_images/', file.filename)
    file.save(file_path)
    buddy = db.get_or_404(Buddy, id)
    buddy.profile_image_url = file.filename
    db.session.commit()
    return {"msg":"Uploaded succesfully","status_code":"200"}

@bp.route('/buddy/<int:id>/image', methods=['GET'])
@cross_origin(origin='*')
def get_buddy_image(id):
    buddy = db.get_or_404(Buddy, id)
    return send_file(os.path.join('buddy_images/',buddy.profile_image_url), mimetype='image/jpeg')  # Adjust mimetype based on your image type


@bp.route('/buddy/<int:id>/services', methods=['GET'])
@cross_origin(origin='*')
def get_buddy_requests(id):
    sr_schema = ServiceRequestSchema(many=True)
    service_requests = db.session.execute(db.select(ServiceRequest).filter_by(buddy_id=id)).scalars()
    return jsonify(sr_schema.dump(service_requests))