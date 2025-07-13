from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from api.config import LOGIN_DATABASE, PASSWORD_DATABASE, HOST_DATABASE, PORT_DATABASE, NAME_DATABASE

engine = create_engine(f"postgresql://{LOGIN_DATABASE}:{PASSWORD_DATABASE}@{HOST_DATABASE}:{PORT_DATABASE}/{NAME_DATABASE}")
base = declarative_base()

class TaskDB(base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    text = Column(String)


Session = sessionmaker(bind=engine)
session = Session()
