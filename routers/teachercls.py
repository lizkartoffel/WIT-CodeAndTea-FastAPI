from fastapi import APIRouter, HTTPException, Depends
from models_schemas import *
from sqlmodel import Session, select
from database import createSession 

router = APIRouter()

@router.get('/teacherclasses/{id}', response_model=ReadTeachercls)
def get_Teachercls(id : int, session: Session = Depends(createSession)):
    teachercls = session.exec(select(TeacherClass).where(TeacherClass.id == id)).one_or_none()
    if teachercls is None:
        raise HTTPException(status_code=404, detail=f"No teacher class with id {id}")
    else: return teachercls 
    

@router.get('/teacherclasses', response_model=list[ReadTeachercls])
def get_all_Teachercls(session: Session = Depends(createSession)):
    all_teachercls = session.exec(select(TeacherClass)).all()
    return all_teachercls


@router.post('/teacherclasses', response_model=ReadTeachercls)
def add_Teachercls(teachercls : CreateTeachercls, session: Session =  Depends(createSession)):

    teacher = session.get(Teacher, teachercls.teacher_id)
    if teacher is None:
        raise HTTPException(status_code=400, detail="Teacher does not exist")

    classroom = session.get(Classroom, teachercls.class_id)
    if classroom is None:
        raise HTTPException(status_code=400, detail="Class does not exist")

    obj = TeacherClass(**teachercls.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)    
    return obj


@router.put('/teacherclasses/{id}', response_model=ReadTeachercls)
def update_Teachercls(id : int, teacherclsupdate : UpdateTeachercls, session: Session = Depends(createSession)):
    teachercls = session.get(TeacherClass, id)
    if teachercls is None:
        raise HTTPException(status_code=404, detail=f"No teacher class with id {id}")
    else:
        teachercls.sqlmodel_update(teacherclsupdate.model_dump(exclude_unset=True))
        session.commit()
        session.refresh(teachercls)
        return teachercls
    

@router.delete('/teacherclasses/{id}', response_model=DeleteResponse)
def delete_Teachercls(id : int, session: Session = Depends(createSession)):
    teachercls = session.get(TeacherClass, id)
    if teachercls is None:
        raise HTTPException(status_code=404, detail=f"No teacher class with id {id}")
    else:
        session.delete(teachercls)
        session.commit()
        return DeleteResponse(message = f"Deleted teacher class with id: {id}")