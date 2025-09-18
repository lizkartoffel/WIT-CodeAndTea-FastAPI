from sqlmodel import SQLModel, Field
from typing import Optional

#table creation

class TeacherClass(SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True, default=None)
    teacher_id : Optional[int] = Field(foreign_key="teacher.id", ondelete="SET NULL")
    class_id : Optional[int] = Field(foreign_key="classroom.id", ondelete="SET NULL")

#schemas creation

class CreateTeachercls (SQLModel):
    teacher_id : int = Field(..., example=1)
    class_id : int = Field(..., example=1)

class ReadTeachercls (SQLModel):
    id : int = Field(..., example=1)
    teacher_id : int = Field(..., example=1)
    class_id : int = Field(..., example=1)


    class Config:
        orm_mode = True

class UpdateTeachercls (SQLModel):
    teacher_id : Optional[int] = Field(None, example=1)
    class_id : Optional[int] = Field(None, example=1)


    class Config:
        orm_mode = True