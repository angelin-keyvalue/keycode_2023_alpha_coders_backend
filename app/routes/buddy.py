from app.routes import bp
from app.models.buddy import Buddy
from werkzeug.security import generate_password_hash,check_password_hash
from flask import request,jsonify
from app.schema.buddy import BuddySchema
from app import db

@bp.route('/buddy', methods=['POST'])
def create_buddy():
    body = request.get_json()
    
    buddy = Buddy(name = body['name'], email=body['email'], password=generate_password_hash(body['password']),gender=body['gender'],phone_number=body['phone_number'],
                  address=body['address'],age=body['age'],city=body['city'])
    db.session.add(buddy)
    id = db.session.commit()
    # print(services[0].amount)
    return {"id":str(id),"status_code":"200"}

@bp.route('/buddy/login', methods=['POST'])
def login_buddy():
    body = request.get_json()
    buddy = db.session.execute(db.select(Buddy).filter_by(email=body['email'])).scalar_one()
    print(buddy)
    if check_password_hash(buddy.password,body['password']) is False:
        return {"msg":"Unauthorized access","status_code":"401"}
    else:
        return {"msg":"Login successful","status_code":"200"}
    
@bp.route('/buddy', methods=['GET'])
def get_buddy():
    buddies_schema = BuddySchema(many=True)
    all_budies = Buddy.query.all()
    return jsonify(buddies_schema.dump(all_budies))