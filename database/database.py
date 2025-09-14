from sqlmodel import SQLModel, create_engine, Session

engine = create_engine("sqlite:///database.db")

def createDB():
    SQLModel.metadata.create_all(engine)

def createSession():
    with Session (engine) as session:
        yield session


        # what is yield and why not return?
        # yield returns our session and closes it automatically (cleanup)
        # while return would require to manually close it using session.close()
        # if forgotten it'll risk having dangling database connections