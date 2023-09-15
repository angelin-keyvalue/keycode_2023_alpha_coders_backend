from app import db
from .basetable import BaseTable


class Document(BaseTable):
    doc_name = db.Column(db.String(128), index=True, unique=True)
    elder_id = db.Column(db.Integer, db.ForeignKey('elder.id'), nullable=False)
    elder = db.relationship('Elder',back_populates='documents')