"""
first task in Python ORM
"""

import MySQLdb
import sys

user = sys.argv[1]
passwd = sys.argv[2]
database = sys.argv[3]
state = sys.argv[4]

db = MySQLdb.connect(user=user, passwd=passwd, database=database)

cur = db.cursor()


def main():
    """
    the main function
    """
    query = """
    SELECT name
    FROM cities
    WHERE state_id = (
        SELECT id
        FROM states
        WHERE name = %s
        );
    """
    cur.execute(query, (state,))
    cities = cur.fetchall()
    for index, city in enumerate(cities):
        print(city[0], end=", " if index < len(cities) - 1 else "\n")



if __name__ == "__main__":
    main()
