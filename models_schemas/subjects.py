from sqlmodel import SQLModel, Field

#table creation

class Subject (SQLModel, table=True):
    id :  int | None = Field(primary_key=True, default=None)
    name : str
    
#schemas creation

class CreateSubject (SQLModel):
    name : str

class ReadSubject (SQLModel):
    id :  int 
    name : str  

class UpdateSubject (SQLModel):
    name : str | None = None