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

    subject = session.get(Subject, teacher.subject_id)
    if subject is None:
        raise HTTPException(status_code=400, detail="Subject does not exist")

    obj = Teacher(**teacher.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)   
    return obj 
    

@router.put('/teachers/{id}', response_model= ReadTeacher)
def update_Teacher(id : int, teacherupdata : UpdateTeacher, session: Session = Depends(createSession)):
    teacher = session.get(Teacher, id)
    if teacher is None:
        raise HTTPException(status_code=404, detail=f"No teacher with id {id}")
    else:
        teacher.sqlmodel_update(teacherupdata.model_dump(exclude_unset=True))

        # Only include fields that were explicitly set when creating the model.
        # Ignore fields that are using their default values (i.e., fields you didn’t touch).
        
        session.commit()
        session.refresh(teacher)
        return teacher
        

@router.delete('/teachers/{id}', response_model= DeleteResponse)
def delete_Teacher(id : int, session : Session = Depends(createSession)):
    teacher = session.get(Teacher, id)
    if teacher is None:
        raise HTTPException(status_code=404, detail=f"No teacher with id {id}")
    else:
        session.delete(teacher)
        session.commit()
        return DeleteResponse(message = f"Deleted teacher with id: {id}")