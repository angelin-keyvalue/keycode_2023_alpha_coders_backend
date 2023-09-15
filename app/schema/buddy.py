
from app.schema import ma
from app.models.buddy import Buddy

class BuddySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Buddy
        # fields =['name','age','address']