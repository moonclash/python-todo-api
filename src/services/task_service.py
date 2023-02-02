from sqlalchemy.orm import Session
from storage import models, schemas
from .utility_classes import UtilsHelper
from .exceptions import TaskNotFoundException

class TaskService:

    @staticmethod
    def build_search_query(criteria):
        search_object = UtilsHelper.get_values_from_dict(criteria)
        search_terms = [
            f"{k} = '{v}'"
            for (k, v) in search_object.items()
        ]
        join_statement = ' AND ' if len(search_terms) > 1 else ''
        return join_statement.join(search_terms)
    
    @staticmethod
    def create_task(db: Session, create_task_dto: schemas.CreateTaskDTO):
        db_task = models.Task(**dict(create_task_dto))
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    
    @staticmethod
    def get_task(db: Session, task_id: str):
        task = db.query(models.Task).get(task_id)
        if not task:
            raise TaskNotFoundException
        return task

    @staticmethod
    def get_tasks_by_criteria(db: Session, criteria) -> List[models.Task] | Task:
        search_statement = TaskService.build_search_query(criteria)
        query = f'SELECT * FROM tasks WHERE {search_statement}' 
        tasks = db.execute(query)
        return tasks.all()
    
    @staticmethod
    def update_task(db: Session, task_id: str, update_task_dto: schemas.UpdateTaskDTO) -> models.Task:
        task_to_update = db.query(models.Task).get(task_id)
        if not task_to_update:
            raise TaskNotFoundException
        values_to_update = UtilsHelper.get_values_from_dict(update_task_dto.dict())
        if values_to_update:
            for key, value in values_to_update.items():
                setattr(task_to_update, key, value)
        db.commit()
        db.refresh(task_to_update)
        return task_to_update
    
    @staticmethod
    def delete_task(db: Session, task_id: str) -> dict:
        task = db.query(models.Task).get(task_id)
        if not task:
            raise TaskNotFoundException
        db.delete(task)
        db.commit()
        return {}
    
