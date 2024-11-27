from app.models import BaseModel
from sqlalchemy import Column, Integer,ForeignKey,DateTime,func

class AsignacionTienda(BaseModel):
    __tablename__ = 'asignaciones_tiendas'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id', ondelete='CASCADE'))
    tienda_id = Column(Integer, ForeignKey('tiendas.id', ondelete='CASCADE'))
    fecha_asignacion = Column(DateTime, default=func.current_timestamp())