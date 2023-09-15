from app.routes import bp
from app.models.services import Services

@bp.route('/services', methods=['GET'])
def get_services():
    services = Services.query.all()
    print(services[0].amount)
    return {"msg":"success","status_code":"200"}