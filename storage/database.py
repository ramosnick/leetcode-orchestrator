from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
from sqlalchemy.engine import Engine
from storage.models import Base


DATABASE_URL = "sqlite:///algo_pod.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":True}) #Engine that manages physical connections to the database

#Decorator that enables foreign key constraints, entries cannot be added to Submissions with an invalid User key.
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

#SessionLocal factory, generates connections via a Python object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def createDB():
    
    inspector = inspect(engine)
    existingTables = inspector.get_table_names()
    
    Base.metadata.create_all(bind=engine)

    if existingTables:
        print(f"Database already initalized.\n Tables:\n{existingTables}")
    else:
        existingTables = inspector.get_table_names()
        print(f"Database tables initalized\n Created Tables:\n{existingTables}")



if __name__ == "__main__":
    createDB()

