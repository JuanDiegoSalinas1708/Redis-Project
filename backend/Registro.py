from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import Usuario
from schemas import UsuarioCreate

init_db()
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/usuarios/")
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return {"message": "Usuario creado", "usuario": nuevo_usuario}
