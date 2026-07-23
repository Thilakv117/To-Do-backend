from typing import Annotated
from fastapi import Depends, FastAPI
from pydantic import BaseModel
import model
from database import engine, sessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

model.BASE.metadata.create_all(bind = engine)

@app.get('/')
def initial():
    return "Welcome to fastapi"


def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()
        
# for dependency injection

db_dependency = Annotated[Session, Depends(get_db)]

# creating a class for task



class TaskCreate(BaseModel):
    title: str
    description: str
    is_completed: bool
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    
@app.post("/task")
def create_user(addTask: TaskCreate, db: db_dependency):
    try:
        db_task = model.Test(
            title = addTask.title,
            description=addTask.description,
            is_completed= addTask.is_completed
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        response = {
            "Data": [db_task]
        }
        return response
    except Exception as e:
        return str(e)

    

