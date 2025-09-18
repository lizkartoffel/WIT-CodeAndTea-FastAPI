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



# and should i add error handling if insertion is done in the wrong order? Done!! in post check if its there THEN add
# do i need error handling for deleting something related to smthing else with a foreign key? rn cant remove student if he has grades for example Done!!
# if i remove error handling for grades, the grades will exist without students? no db error/ this is fine