from sqlmodel import SQLModel, Field
from typing import Optional

#table creation

class Teacher (SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True, default=None)
    name : str
    salary : float
    subject_id : int = Field(foreign_key="subject.id") 

#schemas creation 

class CreateTeacher (SQLModel):
    name : str
    salary : float
    subject_id : int 

class ReadTeacher (SQLModel):
    name : str
    salary : float
    subject_id : int 

class UpdateTeacher (SQLModel):
    name : Optional[str] = None
    salary : Optional[float] = None
    subject_id : Optional[int] = None
