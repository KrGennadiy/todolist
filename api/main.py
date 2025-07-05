from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import uvicorn
'''
app = FastAPI()

engine = create_engine('postgresql://root:root@localhost:5432/to-do-list-db')
print('создал engine\n')
base = declarative_base()
class TaskDB(base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    datetime = Column(String)

Session = sessionmaker(bind=engine)
session = Session()
print('создал сессию')
class Task(BaseModel):
    name: str
    id: int
    datetime: str

@app.post("/postTask/")
def create_task(task: Task):
    try:
        taskdb = TaskDB(name=task.name, datetime=task.datetime, id=task.id)
        session.add(taskdb)
        session.commit()
        return {#"message": taskdb
                print (taskdb)}
    except Exception as e:
        return {#"message": str(e), 
                print (str(e))}
 
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8088)     
'''

app = FastAPI()

engine = create_engine("postgresql://root:root@localhost:5432/testdb")
base = declarative_base()


class TestDB(base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)
    text = Column(String)


Session = sessionmaker(bind=engine)
session = Session()
print("создал сессию")


class Task(BaseModel):
    text: str


@app.post("/postTest/")
async def create_task(test: Task):
    try:
        taskdb = TestDB(text=test.text)
        session.add(taskdb)
        session.commit()
        return {"message": taskdb}
    except Exception as e:
        return {"error": str(e)}