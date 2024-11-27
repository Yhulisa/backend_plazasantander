from app import db
from app.models.centros_comerciales_model import CentroComercialModel
from app.schemas.centros_comerciales_schema import CentroComercialResponseSchema
from http import HTTPStatus


class CentroComercialController:
    def __init__(self):
        self.db = db
        self.model = CentroComercialModel
        self.schema = CentroComercialResponseSchema

    def fetch_all(self, query_params):
        try:
            # Paginación
            # Nro Pagina (a acceder)
            # Nro Registros x Pagina
            # Formula para Offset : ((nº pagina - 1) * nro de registros x pagina)
            '''
                Total 100 centros comerciales
                Pagina 1:
                SELECT * FROM users LIMIT 10 OFFSET 0;

                Pagina 2:
                SELECT * FROM users LIMIT 10 OFFSET 10;
            '''
            page = query_params['page']
            per_page = query_params['per_page']

            records = self.model.where().order_by('id').paginate(
                page=page,
                per_page=per_page
            )
            users = self.schema(many=True)
            return {
                'results': users.dump(records.items),
                'pagination': {
                    'totalRecords': records.total,
                    'totalPages': records.pages,
                    'perPage': records.per_page,
                    'currentPage': records.page
                }
            }, HTTPStatus.OK
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def save(self, body):
        try:
            record_new = self.model.create(**body)
            
            self.db.session.add(record_new)
            self.db.session.commit()
            return {
                'message': f'El centro comercial {body["nombre"]} se creo con exito'
            }, HTTPStatus.CREATED
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def find_by_id(self, id):
        try:
            record = self.model.where(id=id, status=True).first()

            if record:
                user = self.schema(many=False)
                return {
                    'record': user.dump(record)
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro el centro comercial {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def update(self, id, body):
        try:
            record = self.model.where(id=id, status=True).first()

            if record:
                record.update(**body)
                self.db.session.add(record)
                self.db.session.commit()

                return {
                    'message': f'El centro comercial {id}, ha sido actualizado.'
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro el centro comercial {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def remove(self, id):
        try:
            record = self.model.where(id=id, status=True).first()

            if record:
                record.update(status=False)
                self.db.session.add(record)
                self.db.session.commit()

                return {
                    'message': f'El centro comercial {id}, ha sido removido.'
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro el centro comercial {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
