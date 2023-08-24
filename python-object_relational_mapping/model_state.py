"""
model state documentation
"""
from model_state import State
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv


user = argv[1]
passwd = argv[2]
database = argv[3]

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
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, passwd, database))
Session = sessionmaker(bind=engine)
session = Session()

# Import the State class

# Create the table
Base.metadata.create_all(engine)
