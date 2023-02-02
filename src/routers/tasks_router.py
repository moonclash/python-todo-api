from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from services.task_service import TaskNotFoundException, TaskService
from sqlalchemy.orm import Session
from storage.database import SessionLocal
from storage.schemas import CreateTaskDTO, UpdateTaskDTO

task_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@task_router.get('/')
def dead_root():
    return {'hello': 'world'}


@task_router.get('/task/{task_id}', status_code=200)
def get_task_by_id(task_id: UUID, db: Session = Depends(get_db)):
    try:
        return TaskService.get_task(db, task_id)
    except TaskNotFoundException as e:
        raise HTTPException(**{
            'status_code': 404,
            'detail': e.message
        })

@task_router.get('/tasks/')
def search_tasks(title: str = None, description: str = None, completed: bool = False, db: Session = Depends(get_db)):
    search_criteria = {
        'title': title,
        'description': description,
        'completed': completed
    }
    return TaskService.get_tasks_by_criteria(db, search_criteria)


@task_router.post('/task', status_code=201)
def create_task(create_task_dto: CreateTaskDTO, db: Session = Depends(get_db)):
    task = TaskService.create_task(db, create_task_dto)
    return task

@task_router.delete('/task/{task_id}', status_code=204)
def delete_task(task_id: UUID, db: Session = Depends(get_db)):
    try:
        return TaskService.delete_task(db, task_id)
    except TaskNotFoundException as e:
        raise HTTPException(**{
            'status_code': 404,
            'detail': e.message
        })

@task_router.patch('/task/{task_id}', status_code=200)
def update_task(task_id: UUID, update_task_dto: UpdateTaskDTO, db: Session = Depends(get_db)):
    try:
        return TaskService.update_task(db, task_id, update_task_dto)
    except TaskNotFoundException as e:
        raise HTTPException(**{
            'status_code': 404,
            'detail': e.message
        })

@task_router.patch('/task/complete/{task_id}', status_code=200)
def update_task(task_id: UUID, db: Session = Depends(get_db)):
    update_task_dto: UpdateTaskDTO = UpdateTaskDTO()
    update_task_dto.completed = True
    try:
        return TaskService.update_task(db, task_id, update_task_dto)
    except TaskNotFoundException as e:
        raise HTTPException(**{
            'status_code': 404,
            'detail': e.message
        })