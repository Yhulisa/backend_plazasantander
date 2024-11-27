from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.centros_comerciales_model import CentroComercialModel


class CentroComercialRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        return self.namespace.model('CentroComercial Create', {
            'nombre': fields.String(required=True, min_length=3, max_length=100),
            'direccion': fields.String(required=True, min_length=0, max_length=255),
            'logo': fields.String(required=False, min_length=0, max_length=255),
            'telefono': fields.String(required=False, min_length=0, max_length=20),
            'correo': fields.String(required=False, min_length=0, max_length=160),
            'imagen_portada': fields.String(required=False),
            'imagen1': fields.String(required=False),
            'imagen2': fields.String(required=False),
            'imagen3': fields.String(required=False)
        })

    def update(self):
        return self.namespace.model('CentroComercial Update', {
            'nombre': fields.String(required=True, min_length=3, max_length=100),
            'direccion': fields.String(required=True, min_length=0, max_length=255),
            'logo': fields.String(required=False, min_length=0, max_length=255),
            'telefono': fields.String(required=False, min_length=0, max_length=20),
            'correo': fields.String(required=False, min_length=0, max_length=160),
            'imagen_portada': fields.String(required=False),
            'imagen1': fields.String(required=False),
            'imagen2': fields.String(required=False),
            'imagen3': fields.String(required=False)
        })

class CentroComercialResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CentroComercialModel
