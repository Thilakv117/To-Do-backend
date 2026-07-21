from sqlalchemy import Boolean, String, Column, ForeignKey, Integer
from database import BASE

class Test(BASE):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)
    
    