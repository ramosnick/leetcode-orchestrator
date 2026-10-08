from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///algo_pod.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":True}) #Engine that manages physical connections to the database

#SessionLocal factory, generates connections via a Python object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def createDB():
    Base.metadata.create_all(bind=engine)
    print("Database tables initalized")

if __name__ == "__main__":
    createDB()
createDB()
