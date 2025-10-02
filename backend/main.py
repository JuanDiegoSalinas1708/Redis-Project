from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from schemas import UsuarioCreate, UsuarioOut
from crud import crear_usuario, obtener_usuario_por_correo
from passlib.hash import bcrypt
import secrets
from redis_client import r

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="BillCash Backend + Redis 🚀")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:5174"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "BillCash + Redis funcionando 🚀"}

@app.post("/register", response_model=UsuarioOut)
def register(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    if obtener_usuario_por_correo(db, usuario.correo):
        raise HTTPException(status_code=400, detail="Correo ya registrado")
    nuevo_usuario = crear_usuario(db, usuario)
    return nuevo_usuario

@app.post("/login")
def login(
    correo: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    usuario = obtener_usuario_por_correo(db, correo)
    if not usuario or not bcrypt.verify(password, usuario.password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    token = secrets.token_hex(16)
    r.set(token, usuario.id, ex=3600)  # expira en 1 hora
    
    return {"message": "Login exitoso", "token": token}

@app.get("/check-redis/{token}")
def check_redis(token: str):
    usuario_id = r.get(token)
    if usuario_id:
        return {"token": token, "usuario_id": usuario_id.decode()}
    return {"message": "Token inválido o expirado"}
