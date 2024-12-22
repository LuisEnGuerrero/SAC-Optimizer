from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.config import Base
import datetime

# Tabla TipoDocumento como tabla de referencia
class TipoDocumento(Base):
    __tablename__ = "tipo_documento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(3), nullable=False, unique=True, index=True)  # Ejemplo: 'CC', 'TI', 'NIT'
    descripcion = Column(String, nullable=False)  # Ejemplo: 'Cédula de Ciudadanía'

    # Relación con Cliente
    clientes = relationship("Cliente", back_populates="tipo_documento")


# Tabla Cliente: Representa la información básica de un cliente.
class Cliente(Base):
    __tablename__ = 'cliente'

    # Número de documento único que identifica al cliente
    numero_documento = Column(String, primary_key=True)

    # Relación con TipoDocumento
    tipo_documento_id = Column(Integer, ForeignKey('tipo_documento.id'), nullable=False)

    # Información básica del cliente
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    correo = Column(String, nullable=False, unique=True)  # Aseguramos que el correo sea único.
    telefono = Column(String, nullable=False)

    # Relaciones con otras tablas
    tipo_documento = relationship("TipoDocumento", back_populates="clientes")
    compras = relationship("Compra", back_populates="cliente", cascade="all, delete-orphan")
    historiales = relationship("Historial", back_populates="cliente", cascade="all, delete-orphan")


class Producto(Base):
    __tablename__ = 'producto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    talla = Column(String, nullable=True)
    color = Column(String, nullable=True)
    imagen_url = Column(String, nullable=True)  # URL de la imagen del producto


    # Relación con Compra (opcional)
    compras = relationship("Compra", back_populates="producto")


# Tabla Compra: Representa las compras realizadas por los clientes.
class Compra(Base):
    __tablename__ = 'compra'

    # ID único de la compra
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Relación con Cliente
    numero_documento_cliente = Column(String, ForeignKey('cliente.numero_documento'), nullable=False)

    # Relación con Producto
    producto_id = Column(Integer, ForeignKey('producto.id'), nullable=True)

    # Información de la compra
    fecha_compra = Column(DateTime, default=datetime.datetime.utcnow)
    monto = Column(Float, nullable=False)

    # Relación con Cliente y Producto
    cliente = relationship("Cliente", back_populates="compras")
    producto = relationship("Producto", back_populates="compras")


# Tabla Historial: Representa interacciones o eventos asociados con los clientes.
class Historial(Base):
    __tablename__ = 'historial'

    # ID único del historial
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Relación con Cliente
    numero_documento_cliente = Column(String, ForeignKey('cliente.numero_documento'), nullable=False)

    # Información del historial
    fecha_interaccion = Column(DateTime, default=datetime.datetime.utcnow)
    tipo_interaccion = Column(String, nullable=False)

    # Relación con Cliente
    cliente = relationship("Cliente", back_populates="historiales")
