from fastapi import FastAPI, HTTPException
from app.schemas import Student
from app.database import students_db 

app = FastAPI()
# students = []
# home
@app.get("/")
def home():
    return {"message": "API is working!"}

# CREATE
@app.post("/students")
def create_student(student: Student):
    students_db.append(student)
    return {"message": "Student created successfully!", "student": student} 

# READ ALL
@app.get("/students")
def get_students():
    return students_db

# READ ONE (BY INDEX ID)
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id < 0 or student_id >= len(students_db):
        raise HTTPException(status_code=404, detail="Student not found")
    return students_db[student_id]

# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    if student_id < 0 or student_id >= len(students_db):
        raise HTTPException(status_code=404, detail="Student not found")
    students_db[student_id] = updated_student
    return {"message": "Student updated successfully!", "student": updated_student}

# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id < 0 or student_id >= len(students_db):
        raise HTTPException(status_code=404, detail="Student not found")
    deleted_student = students_db.pop(student_id)
    return {"message": "Student deleted successfully!", "student": deleted_student}