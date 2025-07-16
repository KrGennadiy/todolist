from fastapi import APIRouter 
from api.database import TaskDB, session
from schemas import PushTask, DeleteTask

router_tasks = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)

@router_tasks.get("/")
async def tasks_to_front():
    answer = session.query(TaskDB).all()
    return answer


@router_tasks.post("/")
async def createTask(task: PushTask):
    try:
        taskdb = TaskDB(text=task.text)
        session.add(taskdb)
        session.commit()
        return {"message": taskdb}
    except Exception as error:
        return {"error": str(error)}


@router_tasks.delete("/")
async def delete_task(task: DeleteTask):
    try:
        taskdb = TaskDB(id=task.id)
        session.query(TaskDB).filter(TaskDB.id == task.id).delete()
        session.commit()
        return {"message": taskdb}
    except Exception as error:
        return {"error": str(error)}
