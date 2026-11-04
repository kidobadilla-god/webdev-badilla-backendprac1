from sqlmodel import Field , SQLModel

class Student(SQLModel, table=True):
    empid: int | None = Field(default=None, primary_key=True)
    first_name: str
    surname: str
    middle_name: str
    age: int | None = None
    
class Grade(SQLModel, table=True):
    empid: int | None = Field(default=None, primary_key=True)
    type: str
    status: str
    subject: str
    rate: int

class Score(SQLModel, table=True):
    empid: int | None = Field(default=None, primary_key=True)
    score: int 
    Subject: str
    Status: str
    Remarks: str