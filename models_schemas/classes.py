from sqlmodel import SQLModel, Field
from typing import Optional

#table creation

class Classroom (SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True, default=None)
    name :  str

#schemas creation

class ClassCreate (SQLModel):
    name : str

class ClassRead (SQLModel): 
    id: int
    name: str 

class ClassUpdate (SQLModel):
    name: str | None = None   # optional, so user can send only the fields they want