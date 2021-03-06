# db_create.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///mydata.db', echo=True)
Base = declarative_base()

class Names(Base):
  __tablename__ = "namess"
  
  id = Column(Integer, primary_key=True)
  name = Column(String)
  
  def __repr__(self):
    return "{}".format(self.name)
    
 Base.metadata.create_all(engine)