from sqlmodel import SQLModel, Field

#table creation

class Student (SQLModel, table=True):
    id :  int | None = Field(primary_key=True, default=None)
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
    name : str | None = None
    age :  int | None = None
    phone_number : str | None = None
    class_id : int | None = None