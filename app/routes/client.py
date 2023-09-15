from app import db
from app.routes import bp
from app.models.client import Client
from app.schema.client import GetClientSchema

from flask import jsonify

@bp.route('/client/<int:id>', methods=['GET'])
def get_clients(id):
    client = Client.query.one_or_404(id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404
    
    client_schema = GetClientSchema()
    return jsonify(client_schema.dump(client)), 200