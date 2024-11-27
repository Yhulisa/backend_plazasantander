from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.controllers.centros_comerciales_controller import CentroComercialController
from app.schemas.centros_comerciales_schema import CentroComercialRequestSchema


centros_comerciales_ns = api.namespace(
    name='Centros_Comerciales',
    description='Endpoints del modulo Users',
    path='/Centros_Comerciales'
)

request_schema = CentroComercialRequestSchema(centros_comerciales_ns)


@centros_comerciales_ns.route('')

@centros_comerciales_ns.doc(security='Bearer')

class CentrosComericalesListCreate(Resource):
    ''' @jwt_required()'''
    @centros_comerciales_ns.expect(request_schema.all())
    def get(self):
        ''' Listar todos los centros comerciales '''
        query_params = request_schema.all().parse_args()
        controller = CentroComercialController()
        return controller.fetch_all(query_params)

    '''@jwt_required()'''
    @centros_comerciales_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creacion de un centro comercial '''
        controller = CentroComercialController()
        return controller.save(request.json)


@centros_comerciales_ns.route('/<int:id>')
@centros_comerciales_ns.doc(security='Bearer')
class CentrosComercialesGetUpdateDelete(Resource):
    '''@jwt_required()'''
    def get(self, id):
        ''' Obtener un centro comercial  por su id '''
        controller = CentroComercialController()
        return controller.find_by_id(id)

    '''@jwt_required()'''
    @centros_comerciales_ns.expect(request_schema.update(), validate=True)
    def patch(self, id):
        ''' Actualizar un centro comercial  por su id '''
        controller = CentroComercialController()
        return controller.update(id, request.json)

    '''@jwt_required()'''
    def delete(self, id):
        ''' Eliminar un centro comercial  por su id '''
        controller = CentroComercialController()
        return controller.remove(id)
