"""
model state documentation
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the State class
Base = declarative_base()

class State(Base):
    """
    class documentation
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Connect to the MySQL server
engine = create_engine('mysql://username:password@localhost:3306/database_name')
Session = sessionmaker(bind=engine)
session = Session()

# Import the State class
from model_state import State

# Create the table
Base.metadata.create_all(engine)


