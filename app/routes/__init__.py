from flask import Blueprint

bp = Blueprint('api', __name__)

from app.routes import routes