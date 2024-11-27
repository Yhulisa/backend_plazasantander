from app.models import BaseModel
from sqlalchemy import Column,Date,Time, Integer,String,Text,ForeignKey


class Evento(BaseModel):
    __tablename__ = 'eventos'
    id = Column(Integer, primary_key=True)
    centro_comercial_id = Column(Integer, ForeignKey('centros_comerciales.id', ondelete='CASCADE'))
    nombre = Column(String(100), nullable=False)
    titulo = Column(String(100))
    descripcion = Column(Text)
    imagen_principal = Column(String(255))
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
