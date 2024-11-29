from app.models import BaseModel
from sqlalchemy import Column, Integer,ForeignKey

class AsignacionTiendaModel(BaseModel):
    __tablename__ = 'asignaciones_tiendas'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    tienda_id = Column(Integer, ForeignKey('tiendas.id'))