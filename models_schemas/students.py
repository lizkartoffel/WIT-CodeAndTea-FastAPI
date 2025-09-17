from sqlmodel import SQLModel, Field
from typing import Optional
#table creation

class Student (SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True, default=None)
    name : str
    age : int
    phone_number : str | None = None
    class_id :  int = Field(foreign_key="classroom.id") 

#schemas creation

class CreateStudent (SQLModel):
    name : str
    age :  int
    phone_number : str 
    class_id : int 

class ReadStudent (SQLModel):
    id : int
    name : str
    age :  int
    phone_number : str 
    class_id : int 

class UpdateStudent (SQLModel):
    name : Optional[str] = None
    age : Optional[int] = None
    phone_number : Optional[int] = None
    class_id : Optional[int] = None