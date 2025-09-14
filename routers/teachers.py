from fastapi import APIRouter, HTTPException, Depends
from models_schemas import *
from sqlmodel import Session, select
from database import createSession 

router = APIRouter()

@router.get('/teachers/{id}', response_model=ReadTeacher)
def get_Teacher(id : int, session: Session = Depends(createSession)):
    teacher = session.exec(select(Teacher).where(Teacher.id == id)).one_or_none()
    if teacher is None:
        raise HTTPException(status_code=404, detail=f"No teacher with id {id}")
    else: return teacher 

    
@router.get('/teachers', response_model=list [ReadTeacher])
def get_all_Teachers(session : Session = Depends(createSession)):
    all_teachers = session.exec(select(Teacher)).all()
    return all_teachers


@router.post('/teachers', response_model= ReadTeacher)
def add_Teacher(teacher : CreateTeacher, session : Session = Depends(createSession)): 
    obj = Teacher(**teacher.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)    
    

@router.put('/teachers/{id}', response_model= ReadTeacher)
def update_Teacher(id : int, teacherupdata : UpdateTeacher, session: Session = Depends(createSession)):
    teacher = session.get(Teacher, id)
    if teacher is None:
        raise HTTPException(status_code=404, detail=f"No teacher with id {id}")
    else:
        teacher.sqlmodel_update(teacherupdata.model_dump())
        session.commit()
        session.refresh(teacher)
        return teacher
        

@router.delete('/teachers/{id}', response_model= ReadTeacher)
def delete_Teacher(id : int, session : Session = Depends(createSession)):
    teacher = session.get(Teacher, id)
    if teacher is None:
        raise HTTPException(status_code=404, detail=f"No teacher with id {id}")
    else:
        session.delete(teacher)
        session.commit()
        return {"Message" : "Deleted teacher with id: {id}"}