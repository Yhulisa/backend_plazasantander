from app.models import BaseModel
from sqlalchemy import Column, Integer, Date,String,Text,ForeignKey


class PromocionModel(BaseModel):
    __tablename__ = 'promociones'
    id = Column(Integer, primary_key=True)
    tienda_id = Column(Integer, ForeignKey('tiendas.id', ondelete='CASCADE'))
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    imagen = Column(String(255))

