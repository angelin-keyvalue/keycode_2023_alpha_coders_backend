
from app.schema import ma
from app.models.service_request import ServiceRequest

class ServiceRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceRequest