from sqlmodel import SQLModel, Field
from typing import Optional

#table creation

class Grade (SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True, default=None)
    student_id : Optional[int] = Field(foreign_key="student.id", ondelete="SET NULL")
    subject_id : Optional[int] = Field(foreign_key="subject.id", ondelete="SET NULL")
    grade : int 

#schemas creation

class CreateGrade (SQLModel):
    student_id : int = Field(..., example=1)
    subject_id : int = Field(..., example=1)
    grade : int = Field(..., example=80)

class ReadGrade (SQLModel):
    id :  int = Field(..., example=1)
    student_id : int = Field(..., example=1)
    subject_id : int = Field(..., example=1)
    grade : int = Field(..., example=80)

    class Config:
        orm_mode = True

class UpdateGrade (SQLModel):
    student_id : Optional[int] = Field(None, example=1) 
    subject_id : Optional[int] = Field(None, example=1) 
    grade : Optional[int] = Field(None, example=80) 


    class Config:
        orm_mode = True