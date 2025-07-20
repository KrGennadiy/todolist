from fastapi import APIRouter
from database import TaskDB, session
from sqlalchemy.exc import DatabaseError

router_tasks = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)

@router_tasks.get("/")
async def tasks_to_front():
    answer = session.query(TaskDB).all()
    try:
        session.commit()
    except DatabaseError:
        session.rollback()
        return{"error": "database error get task"}
    return answer


@router_tasks.post("/")
async def createTask(task_text: str):
    try:
        taskdb = TaskDB(text=task_text)
        session.add(taskdb)
        try:
            session.commit()
        except DatabaseError:
            session.rollback()
            return{"error": "database error create task"}
        return {"message": taskdb}
    except Exception as error:
        return {"error": str(error)}


@router_tasks.delete("/")
async def delete_task(task_id: int):
    try:
        taskdb = TaskDB(id=task_id)
        session.query(TaskDB).filter(TaskDB.id == task_id).delete()
        try:
            session.commit()
        except DatabaseError:
            session.rollback()
            return{"error": "database error delete task"}
        return {"message": taskdb}
    except Exception as error:
        return {"error": str(error)}
    
@router_tasks.put("/")
async def update_task(task_id: int, task_text: str):
    try:
        taskdb = TaskDB(id=task_id, text=task_text)
        # session.query(TaskDB).filter(TaskDB.id == task_id).update({"text": task_text}, synchronize_session=False)()
        try:
            session.commit()
        except DatabaseError:
            session.rollback()
            return{"error": "database error update task"}
        return {"message": taskdb}
    except Exception as error:
        return {"error": str(error)}
