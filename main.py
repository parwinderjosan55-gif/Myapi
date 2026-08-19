from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select

from database import create_db_and_tables, get_session
from models import Student, StudentCreate, StudentRead, StudentUpdate

app = FastAPI(title="Student API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/students", response_model=StudentRead)
def create_student(student: StudentCreate):
    with get_session() as session:
        db_student = Student.from_orm(student)
        session.add(db_student)
        session.commit()
        session.refresh(db_student)
        return db_student


@app.get("/students", response_model=list[StudentRead])
def list_students():
    with get_session() as session:
        students = session.exec(select(Student)).all()
        return students


@app.get("/students/{student_id}", response_model=StudentRead)
def get_student(student_id: int):
    with get_session() as session:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student


@app.put("/students/{student_id}", response_model=StudentRead)
def update_student(student_id: int, payload: StudentUpdate):
    with get_session() as session:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        student_data = payload.dict(exclude_unset=True)
        for key, value in student_data.items():
            setattr(student, key, value)
        session.add(student)
        session.commit()
        session.refresh(student)
        return student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    with get_session() as session:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        session.delete(student)
        session.commit()
        return {"ok": True}


if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
