from .students import Student,CreateStudent,ReadStudent,UpdateStudent
from .teachers import Teacher,CreateTeacher,ReadTeacher,UpdateTeacher
from .teachercls import TeacherClass,CreateTeachercls,ReadTeachercls,UpdateTeachercls
from .grades import Grade,CreateGrade,ReadGrade,UpdateGrade
from .subjects import Subject,ReadSubject,CreateSubject,UpdateSubject
from .classes import ClassCreate,ClassRead, ClassUpdate,Classroom

# Makes the folder a proper package
# Allows relative imports
# Lets you re-export things for cleaner imports
# W/o it can’t do from routers import * cleanly