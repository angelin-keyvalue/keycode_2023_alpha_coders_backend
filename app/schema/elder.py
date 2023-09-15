from app.schema import ma
from app.models.elder import Elder


class GetElderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Elder
        include_fk = True


class CreateElderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Elder
        exclude = ('id', 'created_at', 'updated_at')