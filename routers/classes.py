from fastapi import APIRouter, HTTPException, Depends
from models_schemas import *
from sqlmodel import Session, select
from database import createSession 

router = APIRouter()

@router.get('/classes/{id}', response_model=ClassRead)
def get_Class(id : int, session: Session = Depends(createSession)):
    classroom = session.exec(select(Classroom).where(Classroom.id == id)).one_or_none()
    if classroom is None:
        raise HTTPException(status_code=404, detail=f"No class with id {id}")
    else: return classroom 


@router.get('/classes', response_model=list[ClassRead])
def get_all_Classes(session: Session = Depends(createSession)):
    all_classes = session.exec(select(Classroom)).all()
    return all_classes


@router.post('/classes', response_model=ClassRead)
def add_Class(classroom : ClassCreate, session: Session = Depends(createSession)):
    obj = Classroom(**classroom.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj    
    

@router.put('/classes/{id}', response_model=ClassRead)
def update_Class(id : int, classupdate : ClassUpdate, session: Session = Depends(createSession)):
    classroom = session.get(Classroom, id)
    if classroom is None:
        raise HTTPException(status_code=404, detail=f"No class with id {id}")
    else:
        classroom.sqlmodel_update(classupdate.model_dump())
        session.commit()
        session.refresh(classroom)
        return classroom
        

@router.delete('/classes/{id}', response_model= dict)
def delete_Class(id : int, session: Session = Depends(createSession)):
    classroom = session.get(Classroom, id)
    if classroom is None:
        raise HTTPException(status_code=404, detail=f"No class with id {id}")
    else:
        session.delete(classroom)
        session.commit()
        return {"Message" : "Deleted classroom with id: {id}"}