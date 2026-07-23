from sqlalchemy import Boolean, String, Column, ForeignKey, Integer
from database import BASE


class Test(BASE):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_completed = Column(Boolean, default=False, index=True)
    
    