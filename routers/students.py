from fastapi import APIRouter, HTTPException, Depends
from models_schemas import *
from sqlmodel import Session, select
from database import createSession 

router = APIRouter()

@router.get('/students/{id}', response_model= ReadStudent)
def get_Student(id : int, session: Session = Depends(createSession)):
    student = session.exec(select(Student).where(Student.id == id)).one_or_none()
    if student is None:
        raise HTTPException(status_code=404, detail=f"No student with id {id}")
    else: return student 


@router.get('/students', response_model=list[ReadStudent])
def get_all_Students(session: Session = Depends(createSession)):
    all_students = session.exec(select(Student)).all()
    return all_students
    

@router.post('/students', response_model= ReadStudent)
def add_Student(student : CreateStudent, session: Session = Depends(createSession)):

    classroom = session.get(Classroom, student.class_id)
    if classroom is None:
        raise HTTPException(status_code=400, detail="Class does not exist") #check if the class id exists before trying to add (bc of foreign key)
    
    
    obj = Student(**student.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj    
    

@router.put('/students/{id}', response_model= ReadStudent)
def update_Student(id : int, studentupdate : UpdateStudent, session: Session = Depends(createSession)):
    student = session.get(Student, id)
    if student is None:
        raise HTTPException(status_code=404, detail=f"No student with id {id}")
    else:
        student.sqlmodel_update(studentupdate.model_dump(exclude_unset=True))
        session.commit()
        session.refresh(student)
        return student
    

@router.delete('/students/{id}', response_model= DeleteResponse)
def delete_Student(id : int, session: Session = Depends(createSession)):
    student = session.get(Student, id)
    if student is None:
        raise HTTPException(status_code=404, detail=f"No student with id {id}")
    else:
        session.delete(student)
        session.commit()
        return DeleteResponse(message = f"Deleted student with id: {id}")