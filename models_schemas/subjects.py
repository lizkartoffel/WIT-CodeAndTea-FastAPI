from sqlmodel import SQLModel, Field
from typing import Optional

#table creation

class Subject (SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True, default=None)
    name : str
    
#schemas creation

class CreateSubject (SQLModel):
    name : str

class ReadSubject (SQLModel):
    id :  int 
    name : str  

class UpdateSubject (SQLModel):
    name : str | None = None