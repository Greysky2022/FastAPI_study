#连接 SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String


engine = create_engine("sqlite:///./sql_app.db", connect_args={"check_same_thread":False})
session = sessionmaker(autocommit=False,bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ ='user'
    id= Column('id',Integer,primary_key=True)
    name = Column('name',String(50),primary_key=True)

Base.metadata.create_all(bind=engine)