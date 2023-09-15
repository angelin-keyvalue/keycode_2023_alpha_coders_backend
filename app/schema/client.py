from app.schema import ma
from app.models.client import Client
from app.schema.elder import GetElderSchema
from marshmallow_sqlalchemy import fields


class GetClientSchema(ma.SQLAlchemyAutoSchema):

    elders = fields.Nested(GetElderSchema, many=True)
    class Meta:
        model = Client
        exclude = ('password',)


class CreateClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client
        exclude = ('id', 'created_at', 'updated_at')


class LoginClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client
        exclude = ('id', 'created_at', 'updated_at', 'full_name', 'contact_number', 'address')
