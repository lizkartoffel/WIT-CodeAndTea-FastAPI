from sqlmodel import SQLModel, Field
from typing import Optional

#table creation

class Teacher (SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True, default=None)
    name : str
    salary : float
    subject_id : Optional[int] = Field(foreign_key="subject.id", ondelete="SET NULL")

#schemas creation 

class CreateTeacher (SQLModel):
    name : str = Field(..., example="ahmed")
    salary : float = Field(..., example=700000)
    subject_id : int = Field(..., example=1)

class ReadTeacher (SQLModel):
    name : str = Field(..., example="ahmed")
    salary : float = Field(..., example=700000)
    subject_id : int = Field(..., example=1)

    class Config:
        orm_mode = True

class UpdateTeacher (SQLModel):
    name : Optional[str] = Field(None, example="ahmed")
    salary : Optional[float] = Field(None, example=700000)
    subject_id : Optional[int] = Field(None, example=1)

    class Config:
        orm_mode = True