from typing import Annotated

from fastapi import Depends, FastAPI
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

