"""
module documentation
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

user = argv[1]
passwd = argv[2]
database = argv[3]

engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost/{}".format(
        user, passwd, database), 
    pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

# Fetch and display all State objects sorted by states.id
states = session.query(State).order_by(State.id).all()

for state in states:
    print(f"{state.id}: {state.name}")

# Close the session
session.close()
