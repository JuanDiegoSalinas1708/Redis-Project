from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    nombres: str
    apellidos: str
    edad: int
    correo: EmailStr
    telefono: str
    numero_documento: str
    tipo_documento: str

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
