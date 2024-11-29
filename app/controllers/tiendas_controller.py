from app import db
from app.models.tiendas_model import TiendaModel
from app.schemas.tiendas_schema import TiendaResponseSchema
from http import HTTPStatus


class TiendaController:
    def __init__(self):
        self.db = db
        self.model = TiendaModel
        self.schema = TiendaResponseSchema

    def fetch_all(self, query_params):
        try:
            # Paginación
            # Nro Pagina (a acceder)
            # Nro Registros x Pagina
            # Formula para Offset : ((nº pagina - 1) * nro de registros x pagina)
            '''
                Total 100 tiendas
                Pagina 1:
                SELECT * FROM tiendas LIMIT 10 OFFSET 0;

                Pagina 2:
                SELECT * FROM tiendas LIMIT 10 OFFSET 10;
            '''
            page = query_params['page']
            per_page = query_params['per_page']

            records = self.model.order_by('id').paginate(
                page=page,
                per_page=per_page
            )
            tiendas = self.schema(many=True)
            return {
                'results': tiendas.dump(records.items),
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
            record_new.hash_password()
            self.db.session.add(record_new)
            self.db.session.commit()
            return {
                'message': f'La tienda {body["nombre"]} se creo con exito'
            }, HTTPStatus.CREATED
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def find_by_id(self, id):
        try:
            record = self.model.where(id=id).first()

            if record:
                user = self.schema(many=False)
                return {
                    'record': user.dump(record)
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro la tienda {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def update(self, id, body):
        try:
            record = self.model.where(id=id).first()

            if record:
                record.update(**body)
                self.db.session.add(record)
                self.db.session.commit()

                return {
                    'message': f'La tienda {id}, ha sido actualizado.'
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro la tienda {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def remove(self, id):
        try:
            record = self.model.where(id=id).first()

            if record:
                record.update(status=False)
                self.db.session.add(record)
                self.db.session.commit()

                return {
                    'message': f'La tienda {id}, ha sido removido.'
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro la tienda {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
