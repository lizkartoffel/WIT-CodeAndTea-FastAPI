from sqlmodel import SQLModel, Field
from typing import Optional

#table creation

class Classroom (SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True, default=None)
    name :  str

#schemas creation

class ClassCreate (SQLModel):
    name : str = Field(..., example="Class 1")

class ClassRead (SQLModel): 
    id: int = Field(..., example=1)
    name: str = Field(..., example="Class 1")
    
    class Config:
        orm_mode = True

class ClassUpdate (SQLModel):
    name: Optional[str] = Field(None, example="Class 2")   # optional, so user can send only the fields they want

    class Config:
        orm_mode = True