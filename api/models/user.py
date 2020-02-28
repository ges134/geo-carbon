from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class User(Base):
  __tablename__ = 'Users'

  id = Column(Integer, primary_key=True)
  email = Column(String(50), unique=True)
  password = Column(String(70))