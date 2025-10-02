from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Variables de entorno
DB_USER = os.getenv("DB_USER", "root")  # Usuario MySQL
DB_PASSWORD = os.getenv("DB_PASSWORD", "")  # Contraseña (por defecto vacío en XAMPP)
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")  # Host de MySQL
DB_PORT = os.getenv("DB_PORT", "3306")  # Puerto por defecto
DB_NAME = os.getenv("DB_NAME", "billcash")  # Base de datos

# URL de conexión para SQLAlchemy
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear motor y sesión
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Muestra los queries en consola
    pool_pre_ping=True  # Evita errores de conexión caida
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        print("Base de datos inicializada correctamente ✅")
    except Exception as e:
        print("Error al inicializar la base de datos:", e)
