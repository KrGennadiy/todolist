from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import uvicorn

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
engine = create_engine("postgresql://postgres:root@localhost:5432/tododb")
base = declarative_base()


class TaskDB(base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    text = Column(String)


Session = sessionmaker(bind=engine)
session = Session()


class Task(BaseModel):
    text: str
    id: int | None = None


class PushTask(BaseModel):
    text: str

class DeleteTask(BaseModel):
    id: int

@app.post("/pullTask")
async def toFrontTasks():
    answer = session.query(TaskDB).all()
    return answer


@app.post("/pushTask")
async def createTask(task: PushTask):
    try:
        taskdb = TaskDB(text=task.text)
        session.add(taskdb)
        session.commit()
        return {"message": taskdb}
    except ValidationError as e:
        return {"error": e.errors()}


@app.post("/deleteTask")
async def delete_task(task: DeleteTask):
    try:
        taskdb = TaskDB(id=task.id)
        session.query(TaskDB).filter(TaskDB.id == task.id).delete()
        session.commit()
        return {"message": taskdb}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8088)
