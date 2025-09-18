from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import event

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# Enable foreign key enforcement in SQLite
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# engine = create_engine("sqlite:///database.db")


def createDB():
    SQLModel.metadata.create_all(engine)

def createSession():
    with Session (engine) as session:
        yield session


        # what is yield and why not return?
        # yield returns our session and closes it automatically (cleanup)
        # while return would require to manually close it using session.close()
        # if forgotten it'll risk having dangling database connections