"""
module documentation
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import Base and State from model_state module
from model_state import Base, State


class QueryStatesWithA:
    """
    A class to query and print State objects
    containing the letter "a" from the database.

    Attributes:
        mysql_username (str): MySQL username.
        mysql_password (str): MySQL password.
        database_name (str): Database name.
    """

    def __init__(self, mysql_username, mysql_password, database_name):
        self.mysql_username = mysql_username
        self.mysql_password = mysql_password
        self.database_name = database_name
        self.engine = create_engine(
            'mysql://{}:{}@localhost:3306/{}'.format(
                mysql_username, mysql_password, database_name))
        self.Session = sessionmaker(bind=self.engine)

    def print_states_with_a(self):
        """
        Prints State objects containing the letter "a" from the database.
        """
        session = self.Session()
        states_with_a = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()
        session.close()

        for state in states_with_a:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    # Replace with your MySQL credentials and database name
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    query = QueryStatesWithA(mysql_username, mysql_password, database_name)
    query.print_states_with_a()
