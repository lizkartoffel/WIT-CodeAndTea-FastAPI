from fastapi import FastAPI
from database import createDB
from routers import *  # from routers import students,teachers,subjects

createDB()

app = FastAPI()

@app.get("/")
def testing():
    return "hi"

app.include_router(students.router)
app.include_router(teachers.router)
app.include_router(subjects.router)
app.include_router(grades.router)
app.include_router(classes.router)
app.include_router(teachercls.router)

# because of foreign keys there should be an order to input data w/o causing issues 
# Classes → Subjects → Teachers → Students → TeacherCls → Grades

# what about deleteing a class if there's students in it?
# and should i add error handling if insertion is done in the wrong order?