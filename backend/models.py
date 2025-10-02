from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
    telefono = Column(String, nullable=False)
    numero_documento = Column(String, unique=True, nullable=False)
    tipo_documento = Column(String, nullable=False)
    password = Column(String, nullable=False)
