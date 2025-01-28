from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite3', echo=True) # logar os sqls

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False, # enviar dados antes consulta
                            bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
