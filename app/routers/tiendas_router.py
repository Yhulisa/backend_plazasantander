from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.controllers.tiendas_controller import TiendaController
from app.schemas.tiendas_schema import TiendaRequestSchema


tienda_ns = api.namespace(
    name='Tiendas',
    description='Endpoints del modulo Tiendas',
    path='/tiendas'
)

request_schema = TiendaRequestSchema(tienda_ns)


@tienda_ns.route('')

@tienda_ns.doc(security='Bearer')

class TiendasListCreate(Resource):
    '''@jwt_required()'''
    @tienda_ns.expect(request_schema.all())
    def get(self):
        ''' Listar todos las tiendas '''
        query_params = request_schema.all().parse_args()
        controller = TiendaController()
        return controller.fetch_all(query_params)

    '''@jwt_required()'''
    @tienda_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creacion de una tienda '''
        controller = TiendaController()
        return controller.save(request.json)


@tienda_ns.route('/<int:id>')
@tienda_ns.doc(security='Bearer')
class TiendasGetUpdateDelete(Resource):
    '''@jwt_required()'''
    def get(self, id):
        ''' Obtener una tienda por su id '''
        controller = TiendaController()
        return controller.find_by_id(id)

    '''@jwt_required()'''
    @tienda_ns.expect(request_schema.update(), validate=True)
    def patch(self, id):
        ''' Actualizar una tienda por su id '''
        controller = TiendaController()
        return controller.update(id, request.json)

    '''@jwt_required()'''
    def delete(self, id):
        ''' Eliminar una tienda por su id '''
        controller = TiendaController()
        return controller.remove(id)
