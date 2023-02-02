from fastapi import FastAPI
from storage.database import Base, engine
from routers.tasks_router import task_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(task_router)