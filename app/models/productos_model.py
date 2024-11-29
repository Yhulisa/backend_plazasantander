from app.models import BaseModel
from sqlalchemy import Column, Integer,String,ForeignKey

class Producto(BaseModel):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    tienda_id = Column(Integer, ForeignKey('tiendas.id'))
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(100))
    imagen1 = Column(String(255))

