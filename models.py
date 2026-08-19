from typing import Optional
from sqlmodel import Field, SQLModel


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int] = None
    email: Optional[str] = None
    major: Optional[str] = None


class StudentCreate(SQLModel):
    name: str
    age: Optional[int] = None
    email: Optional[str] = None
    major: Optional[str] = None


class StudentRead(SQLModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None
    major: Optional[str] = None


class StudentUpdate(SQLModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    major: Optional[str] = None
