from sqlmodel import SQLModel, Field

#table creation

class TeacherClass(SQLModel, table=True):
    id : int | None = Field(primary_key=True, default=None)
    teacher_id : int = Field(foreign_key="teacher.id")
    class_id : int = Field(foreign_key="classroom.id")

#schemas creation

class CreateTeachercls (SQLModel):
    teacher_id : int
    class_id : int 

class ReadTeachercls (SQLModel):
    id : int
    teacher_id : int
    class_id : int 

class UpdateTeachercls (SQLModel):
    teacher_id : int | None = None
    class_id : int | None = None