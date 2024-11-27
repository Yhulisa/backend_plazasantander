from app.models import BaseModel
from sqlalchemy import Column, Integer, String,Text
from sqlalchemy.orm import relationship

class CentroComercialModel(BaseModel):
    __tablename__ = 'centros_comerciales'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(Text, nullable=False)
    logo = Column(String(255))
    telefono = Column(String(20))
    correo = Column(String(100))
    imagen_portada = Column(String(255))
    imagen1 = Column(String(255))
    imagen2 = Column(String(255))
    imagen3 = Column(String(255))

    '''tiendas = relationship('TiendaModel', backref='centro_comercial', cascade="all, delete")'''
