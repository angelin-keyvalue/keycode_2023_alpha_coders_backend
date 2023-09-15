from flask import Blueprint

bp = Blueprint('api', __name__)

from app.routes import buddy, client, elder, service_request, document
