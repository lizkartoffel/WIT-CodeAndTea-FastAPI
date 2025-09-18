from sqlmodel import SQLModel, Field
from typing import Optional

#table creation

class Subject (SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True, default=None)
    name : str
    
#schemas creation

class CreateSubject (SQLModel):
    name : str = Field(..., example="ahmed")

class ReadSubject (SQLModel):
    id :  int = Field(..., example=1)
    name : str  = Field(..., example="ahmed")

    class Config:
        orm_mode = True

class UpdateSubject (SQLModel):
    name : Optional[str] = Field(None, example="ahmed")

    class Config:
        orm_mode = True