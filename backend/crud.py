from sqlalchemy.orm import Session
from models import Usuario
from schemas import UsuarioCreate
from passlib.hash import bcrypt

def obtener_usuario_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()

def crear_usuario(db: Session, usuario: UsuarioCreate):
    hashed_password = bcrypt.hash(usuario.password)
    db_usuario = Usuario(
        nombres=usuario.nombres,
        apellidos=usuario.apellidos,
        edad=usuario.edad,
        correo=usuario.correo,
        telefono=usuario.telefono,
        numero_documento=usuario.numero_documento,
        tipo_documento=usuario.tipo_documento,
        password=hashed_password,
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
