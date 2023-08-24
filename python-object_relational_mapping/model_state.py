"""
model state documentation
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Represents a state entity in the MySQL table 'states'.

    Attributes:
    id (int): An auto-generated, unique integer representing the primary key.
    name (str): A string with a maximum of 128 characters representing the state name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
