from app.schema import ma
from app.models.client import Client


class GetClientSchema(ma.Schema):
    class Meta:
        model = Client
        fields = ('id','full_name','email','contact_number','address','created_at')