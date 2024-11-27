from app.models import BaseModel
from sqlalchemy import Column, Integer,String,Text,ForeignKey

class Producto(BaseModel):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    tienda_id = Column(Integer, ForeignKey('tiendas.id', ondelete='CASCADE'))
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    imagen1 = Column(String(255))

