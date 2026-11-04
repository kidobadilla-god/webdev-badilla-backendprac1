from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine

from models import  Student

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": "Hello Worldiojnhiuhiu"}


@app.get("/Student/{id}")
async def read_student(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        std = session.get(Student, id)
        return {"message": std}
    

@app.post("/Student")
async def root(Student  : Student):
    with Session(engine) as session:
        session.add(Student)
        session.commit()
        session.refresh(Student)

        return {"message": 'created'}
    

from models import  Grade

@app.get("/Grade/{id}")
async def read_grade(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        grd = session.get(Grade, id)
        return {"message": grd}
    

@app.post("/Grade")
async def root(Grade  : Grade):
    with Session(engine) as session:
        session.add(Grade)
        session.commit()
        session.refresh(Grade)

        return {"message": 'created'}
    
from models import  Score

@app.get("/Score/{id}")
async def read_score(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        scr = session.get(Score, id)
        return {"message": scr}
    

@app.post("/Score")
async def root(Score  : Score):
    with Session(engine) as session:
        session.add(Score)
        session.commit()
        session.refresh(Score)

        return {"message": 'created'}