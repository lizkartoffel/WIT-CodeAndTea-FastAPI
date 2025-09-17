from sqlmodel import SQLModel, Field
from typing import Optional

#table creation

class Grade (SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True, default=None)
    student_id : int = Field(foreign_key="student.id")
    subject_id : int = Field(foreign_key="subject.id")
    grade : int 

#schemas creation

class CreateGrade (SQLModel):
    student_id : int
    subject_id : int 
    grade : int

class ReadGrade (SQLModel):
    id :  int
    student_id : int
    subject_id : int 
    grade : int

class UpdateGrade (SQLModel):
    student_id : Optional[int] = None
    subject_id : Optional[int] = None
    grade : Optional[int] = None 