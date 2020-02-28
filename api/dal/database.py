from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://Geocarbon:@pp@cc355@localhost/geocarbon"

def getSession():
  engine = create_engine(SQLALCHEMY_DATABASE_URL)
  return sessionmaker(bind=engine)()