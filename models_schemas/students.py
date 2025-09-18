from sqlmodel import SQLModel, Field
from typing import Optional
#table creation

class Student (SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True, default=None)
    name : str
    age : int
    phone_number : str | None = None
    class_id :  Optional[int] = Field(foreign_key="classroom.id", ondelete="SET NULL") 

#schemas creation

class CreateStudent (SQLModel):
    name : str = Field(..., example="ahmed")
    age :  int = Field(..., example=19)
    phone_number : str = Field(..., example="+964 123 1234")
    class_id : int = Field(..., example=1)

class ReadStudent (SQLModel):
    id : int = Field(..., example=1)
    name : str = Field(..., example="ahmed")
    age :  int = Field(..., example=19)
    phone_number : str = Field(..., example="+964 123 1234")
    class_id : int = Field(..., example=1)


    class Config:
        orm_mode = True

class UpdateStudent (SQLModel):
    name : Optional[str] = Field(None, example="ahmed")
    age : Optional[int] = Field(None, example=19)
    phone_number : Optional[str] = Field(None, example="+964 123 1234")
    class_id : Optional[int] = Field(None, example=1)

    class Config:
        orm_mode = True