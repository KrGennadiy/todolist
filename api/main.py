# import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers.tasks import router_tasks

# sys.path.append('C:/dev/todolist')

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_tasks)
app.get('/')
async def root():
    return {"message": "root is work"}

if __name__ == "__main__":
    uvicorn.run('main:app', host="localhost", port=8088, reload=True)
