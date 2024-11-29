from app.models import BaseModel
from sqlalchemy import Column,Date,Time, Integer,String,Text,ForeignKey


class EventoModel(BaseModel):
    __tablename__ = 'eventos'
    id = Column(Integer, primary_key=True)
    centro_comercial_id = Column(Integer, ForeignKey('centros_comerciales.id'))
    nombre = Column(String(100), nullable=False)
    titulo = Column(String(100))
    descripcion = Column(String(255))
    imagen_principal = Column(String(255))
    fecha_hora =  Column(String(255))
