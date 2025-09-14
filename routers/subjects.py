from fastapi import APIRouter, HTTPException, Depends
from models_schemas import *
from sqlmodel import Session, select
from database import createSession 

router = APIRouter()

@router.get('/subjects/{id}', response_model=ReadSubject)
def get_Subject(id : int, session: Session = Depends(createSession)):
    subject = session.exec(select(Subject).where(Subject.id == id)).one_or_none()
    if subject is None:
        raise HTTPException(status_code=404, detail=f"No subject with id {id}")
    else: return subject 
    

@router.get('/subjects', response_model=list[ReadSubject])
def get_all_Subjects(session: Session = Depends(createSession)):
    all_subjects = session.exec(select(Subject)).all()
    return all_subjects
    

@router.post('/subjects', response_model=ReadSubject)
def add_Subject(subject : CreateSubject, session: Session = Depends(createSession)):
    obj = Subject(**subject.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)    


@router.put('/subjects/{id}', response_model=ReadSubject)
def update_Subject(id : int, subjectupdate : UpdateSubject, session: Session = Depends(createSession)):
    subject = session.get(Subject, id)
    if subject is None:
        raise HTTPException(status_code=404, detail=f"No subject with id {id}")
    else:
        subject.sqlmodel_update(subjectupdate.model_dump())
        session.commit()
        session.refresh(subject)
        return subject
        

@router.delete('/subjects/{id}', response_model=dict)
def delete_Subject(id : int, session: Session = Depends(createSession)):
    subject = session.get(Subject, id)
    if subject is None:
        raise HTTPException(status_code=404, detail=f"No subject with id {id}")
    else:
        session.delete(subject)
        session.commit()
        return {"Message" : "Deleted subject with id: {id}"}