"""
module docs
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
# Import Base and State from model_state module
from model_state import Base, State


class QueryFirstState:
    """
    A class to query and print the first State object from the database.

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
            f'mysql://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')
        self.Session = sessionmaker(bind=self.engine)

    def print_first_state(self):
        """
        Prints the first State object from the database.
        """
        session = self.Session()
        first_state = session.query(State).order_by(State.id).first()
        session.close()

        if first_state is None:
            print("Nothing")
        else:
            print(f"{first_state.id}: {first_state.name}")


if __name__ == "__main__":
    # Replace with your MySQL credentials and database name
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    query = QueryFirstState(mysql_username, mysql_password, database_name)
    query.print_first_state()
