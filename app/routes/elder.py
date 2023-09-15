from app import db
from app.routes import bp
from app.models.elder import Elder
from app.models.client import Client
from app.schema.elder import (GetElderSchema, CreateElderSchema)

from flask import jsonify, request
from werkzeug.security import generate_password_hash,check_password_hash


@bp.route('/elder/<int:id>', methods=['GET'])
def get_elder(id):
    elder = Elder.query.get(id)
    if not elder:
        return jsonify({'error': 'Elder not found'}), 404

    elder_schema = GetElderSchema()
    return jsonify(elder_schema.dump(elder)), 200


@bp.route('/elder', methods=['POST'])
def create_elder():
    try:
        create_elder_schema = CreateElderSchema()
        elder_data = create_elder_schema.load(request.get_json())
        client_id = request.args.get('client_id')
        try:
            client = Client.query.get(client_id)
            if not client:
                return jsonify({'error': 'Client not found'}), 404
            elder_data['client_id'] = client_id
        except Exception:
            return jsonify({'error': 'Client not found'}), 404
        else:
            new_elder = Elder(**elder_data)
            db.session.add(new_elder)
            db.session.commit()
            return jsonify({'message': 'Register Success', 'id': new_elder.id}), 200
    except Exception:
        db.session.rollback()
        return jsonify({'error': 'Something went wrong'}), 404
