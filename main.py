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
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None
    
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
    
@app.delete("/task/{id}")
def task_delete(id:int, db: db_dependency):
    try:
        delete_task = db.query(model.Test).filter(model.Test.id == id).first()
        db.delete(delete_task)
        db.commit()
        
        return "Deleted successfuly"
    except Exception as e:
        return {"eMessage": str(e)}
    
@app.get("/task")
def get_task(db: db_dependency):
    try:
        tasks = model.Test
        users = db.query(tasks).all()
        return users
    except Exception as e:
        return {
            "eMessage": str(e)
        }
        
@app.patch("/task/{id}")
def update_task(id: int, updateTask: TaskCreate, db: db_dependency):
    try:
        filter_task = db.query(model.Test).filter(model.Test.id == id).first()
        if filter_task is None:
            return {
                "eMesage": f"{id} not found"
            }
        update_data = updateTask.model_dump(exclude_unset=True)
        update_data = updateTask.model_dump(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(filter_task, key, value)
        db.commit()
        db.refresh(filter_task)
    
        return {
            "data": filter_task
        }
    except Exception as e:
        return {"eMessage": e}
    
    
                
    
    
    


    

    

