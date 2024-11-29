from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.eventos_model import EventoModel


class UserRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        return self.namespace.model('Evento Create', {
            'centro_comercial_id': fields.Integer(required=True),
            'nombre': fields.String(required=True, min_length=3, max_length=100),
            'titulo': fields.String(required=True, min_length=3, max_length=100),
            'descripcion': fields.String(required=False, min_length=0, max_length=255),
            'imagen_principal': fields.String(required=False, min_length=0, max_length=255),
            'fecha_hora': fields.String(required=False, min_length=0, max_length=255)
        })

    def update(self):
        return self.namespace.model('Evento Update', {
            'centro_comercial_id': fields.Integer(required=True),
            'nombre': fields.String(required=True, min_length=3, max_length=100),
            'titulo': fields.String(required=True, min_length=3, max_length=100),
            'descripcion': fields.String(required=False, min_length=0, max_length=255),
            'imagen_principal': fields.String(required=False, min_length=0, max_length=255),
            'fecha_hora': fields.String(required=False, min_length=0, max_length=255)
        })


class EventoResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EventoModel
        include_fk = True

    centro_comercial = Nested('CentroComercialResponseSchema', many=False)
