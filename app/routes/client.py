from app import db
from app.routes import bp
from app.models.client import Client
from app.schema.client import (GetClientSchema, CreateClientSchema, LoginClientSchema)

from flask import jsonify, request
from werkzeug.security import generate_password_hash,check_password_hash


@bp.route('/client/login', methods=['POST'])
def login():
    login_client_schema = LoginClientSchema()
    login_data = login_client_schema.load(request.get_json())
    try:
        client = db.session.execute(db.select(Client).filter_by(email=login_data['email'])).scalar_one()
    except Exception as exc:
        return jsonify({"msg":"Login failed"}), 401

    if check_password_hash(client.password,login_data['password']):
        return jsonify({"msg":"Login successful", "id": client.id}), 200
    else:
        return jsonify({"msg":"Login failed"}), 401


@bp.route('/client/<int:id>', methods=['GET'])
def get_client(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404
    
    client_schema = GetClientSchema()
    return jsonify(client_schema.dump(client)), 200


@bp.route('/client', methods=['POST'])
def create_client():
    try:
        create_client_schema = CreateClientSchema()
        client_data = create_client_schema.load(request.get_json())
        client_data['password'] = generate_password_hash(client_data['password'])
        new_client = Client(**client_data)
        db.session.add(new_client)
        db.session.commit()
        return jsonify({'message': 'Register Success', 'id': new_client.id}), 200
    except Exception:
        db.session.rollback()
        return jsonify({'error': 'Something went wrong'}), 404
