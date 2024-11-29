from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.tiendas_model import TiendaModel


class TiendaRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        return self.namespace.model('Tienda Create', {
            'centro_comercial_id': fields.Integer(required=True),
            'numero_tienda': fields.Integer(required=False),
            'nombre': fields.String(required=True, min_length=3, max_length=100),
            'logo': fields.String(required=False, min_length=0, max_length=255),
            'telefono': fields.String(required=False, min_length=0, max_length=20),
            'dias_abiertos': fields.String(required=False, min_length=0, max_length=50),
            'horario': fields.String(required=False, min_length=0, max_length=255),
            'numero_piso': fields.Integer(required=False),
            'titulo': fields.String(required=False, min_length=0, max_length=100),
            'descripcion': fields.String(required=False, min_length=0, max_length=255),
            'imagen_portada': fields.Integer(required=True),
            'imagen1': fields.String(required=False, min_length=0, max_length=255),
            'imagen2': fields.String(required=False, min_length=0, max_length=255),
            'imagen3': fields.String(required=False, min_length=0, max_length=255),
            'tamanio': fields.Decimal(required=False),
            'tiene_bano': fields.Boolean(required=False),
            'tiene_almacen': fields.Boolean(required=False),
            'precio_estimado': fields.Decimal(required=False),
            'esta_alquilada': fields.Boolean(required=False),
            'contrato_vigente': fields.Boolean(required=False),
            'disponibilidad_contacto':fields.String(required=False, min_length=0, max_length=100),
        })

    def update(self):
        return self.namespace.model('Tienda Update', {
                        'centro_comercial_id': fields.Integer(required=True),
            'numero_tienda': fields.Integer(required=False),
            'nombre': fields.String(required=True, min_length=3, max_length=100),
            'logo': fields.String(required=False, min_length=0, max_length=255),
            'telefono': fields.String(required=False, min_length=0, max_length=20),
            'dias_abiertos': fields.String(required=False, min_length=0, max_length=50),
            'horario': fields.String(required=False, min_length=0, max_length=255),
            'numero_piso': fields.Integer(required=False),
            'titulo': fields.String(required=False, min_length=0, max_length=100),
            'descripcion': fields.String(required=False, min_length=0, max_length=255),
            'imagen_portada': fields.Integer(required=True),
            'imagen1': fields.String(required=False, min_length=0, max_length=255),
            'imagen2': fields.String(required=False, min_length=0, max_length=255),
            'imagen3': fields.String(required=False, min_length=0, max_length=255),
            'tamanio': fields.Decimal(required=False),
            'tiene_bano': fields.Boolean(required=False),
            'tiene_almacen': fields.Boolean(required=False),
            'precio_estimado': fields.Decimal(required=False),
            'esta_alquilada': fields.Boolean(required=False),
            'contrato_vigente': fields.Boolean(required=False),
            'disponibilidad_contacto':fields.String(required=False, min_length=0, max_length=100),
        })


class TiendaResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TiendaModel
        include_fk = True

    centro_comercial = Nested('CentroComercialResponseSchema', many=False)
