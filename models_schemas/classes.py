from sqlmodel import SQLModel, Field

#table creation

class Classroom (SQLModel, table=True):
    id :  int | None = Field(primary_key=True, default=None)
    name :  str

#schemas creation

class ClassCreate (SQLModel):
    name : str

class ClassRead (SQLModel): 
    id: int
    name: str 

class ClassUpdate (SQLModel):
    name: str | None = None   # optional, so user can send only the fields they want