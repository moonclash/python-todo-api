from fastapi import FastAPI
from fastapi.testclient import TestClient
from storage.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from routers.tasks_router import task_router
import pytest
from typing import Any
from typing import Generator
from storage.database import Base

def start_app():
    app = FastAPI()
    app.include_router(task_router)
    return app

SQLALCHEMY_DATABASE_URL = 'postgresql://superuser:topsecret@test_database/db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    Base.metadata.create_all(engine)
    _app = start_app()
    yield _app
    


@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    session = SessionTesting(bind=connection)
    yield session 
    session.close()
    connection.close()


@pytest.fixture(scope="function")
def test_client(
    app: FastAPI, db_session: SessionTesting
) -> Generator[TestClient, Any, None]:

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client