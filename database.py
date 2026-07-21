from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://postgres:sakthi635109@localhost:5432/test'

engine = create_engine(URL_DATABASE)

sessionLocal = sessionmaker(autoflush=False, autocommit = False,bind=engine)

BASE = declarative_base()
