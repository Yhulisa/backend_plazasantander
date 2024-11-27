from app.models import BaseModel
from sqlalchemy import Column, Integer,Numeric, String, Boolean,Text,ForeignKey
from sqlalchemy.orm import relationship

class TiendaModel(BaseModel):
    __tablename__ = 'tiendas'
    id = Column(Integer, primary_key=True)
    centro_comercial_id = Column(Integer, ForeignKey('centros_comerciales.id', ondelete='CASCADE'))
    numero_tienda = Column(String(20), nullable=False)
    nombre = Column(String(100), nullable=False)
    logo = Column(String(255))
    telefono = Column(String(20))
    dias_abiertos = Column(String(50))
    horario = Column(Text)
    numero_piso = Column(Integer, nullable=False)
    titulo = Column(String(100))
    descripcion = Column(Text)
    imagen_portada = Column(String(255))
    imagen1 = Column(String(255))
    imagen2 = Column(String(255))
    imagen3 = Column(String(255))
    tamanio = Column(Numeric(10, 2))
    tiene_bano = Column(Boolean, default=False)
    tiene_almacen = Column(Boolean, default=False)
    precio_estimado = Column(Numeric(12, 2))
    esta_alquilada = Column(Boolean, default=False)
    contrato_vigente = Column(Boolean, default=False)
    disponibilidad_contacto = Column(String(100))

    productos = relationship('ProductoModel', backref='tienda', cascade="all, delete")
    promociones = relationship('PromocionModel', backref='tienda', cascade="all, delete")



'''
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    es_administrador = db.Column(db.Boolean, default=False)

    asignaciones = db.relationship('AsignacionTienda', backref='usuario', cascade="all, delete")
'''
