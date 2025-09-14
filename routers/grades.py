from fastapi import APIRouter, HTTPException, Depends
from models_schemas import *
from sqlmodel import Session, select
from database import createSession 

router = APIRouter()

@router.get('/grades/{id}', response_model=ReadGrade)
def get_Grade(id : int, session: Session =  Depends(createSession)):
    grade = session.exec(select(Grade).where(Grade.id == id)).one_or_none()
    if grade is None:
        raise HTTPException(status_code=404, detail=f"No grade with id {id}")
    else: return grade 


@router.get('/grades', response_model=list[ReadGrade])
def get_all_Grades(session: Session = Depends(createSession)):
    all_grades = session.exec(select(Grade)).all()
    return all_grades
    

@router.post('/grades', response_model=ReadGrade)
def add_Grade(grade : CreateGrade, session: Session = Depends(createSession)):
    obj = Grade(**grade.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)    


@router.put('/grades/{id}', response_model=ReadGrade)
def update_Grade(id : int, gradeupdate : UpdateGrade, session: Session = Depends(createSession)):
    grade = session.get(Grade, id)
    if grade is None:
        raise HTTPException(status_code=404, detail=f"No class with id {id}")
    else:
        grade.sqlmodel_update(gradeupdate.model_dump())
        session.commit()
        session.refresh(grade)
        return grade
        

@router.delete('/grades/{id}', response_model=dict)
def delete_Grade(id : int, session: Session = Depends(createSession)):
    grade = session.get(Grade, id)
    if grade is None:
        raise HTTPException(status_code=404, detail=f"No class with id {id}")
    else:
        session.delete(grade)
        session.commit()
        return {"Message" : "Deleted grade with id: {id}"}