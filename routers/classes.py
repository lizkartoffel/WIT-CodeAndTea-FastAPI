from fastapi import APIRouter, HTTPException, Depends
from models_schemas import *
from sqlmodel import Session, select
from database import createSession 

router = APIRouter()

@router.get('/classes/{id}', response_model=ClassRead)
def get_class(id : int, session: Session = Depends(createSession)):
    classroom = session.exec(select(Classroom).where(Classroom.id == id)).one_or_none()
    if classroom is None:
        raise HTTPException(status_code=404, detail=f"No class with id {id}")
    else: return classroom 


@router.get('/classes', response_model=list[ClassRead])
def get_classes(session: Session = Depends(createSession)):
    all_classes = session.exec(select(Classroom)).all()
    return all_classes


@router.post('/classes', response_model=ClassRead)
def add_class(classroom : ClassCreate, session: Session = Depends(createSession)):
    obj = Classroom(**classroom.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj    
    

@router.put('/classes/{id}', response_model=ClassRead)
def update_class(id : int, classupdate : ClassUpdate, session: Session = Depends(createSession)):
    classroom = session.get(Classroom, id)
    if classroom is None:
        raise HTTPException(status_code=404, detail=f"No class with id {id}")
    else:
        classroom.sqlmodel_update(classupdate.model_dump(exclude_unset=True))
        session.commit()
        session.refresh(classroom)
        return classroom
        

@router.delete('/classes/{id}', response_model= DeleteResponse)
def delete_class(id : int, session: Session = Depends(createSession)):
    classroom = session.get(Classroom, id)
    if classroom is None:
        raise HTTPException(status_code=404, detail=f"No class with id {id}")
    else:
        session.delete(classroom)
        session.commit()
        return DeleteResponse(message = f"Deleted classroom with id: {id}")