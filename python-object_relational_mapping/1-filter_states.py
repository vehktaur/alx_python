"""
first task in Python ORM
"""

import MySQLdb
import sys

user = sys.argv[1]
passwd = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(user=user, passwd=passwd, database=database)

cur = db.cursor()


def main():
    """
    the main function
    """
    query = "SELECT * FROM states ORDER BY id;"
    cur.execute(query)
    rows = list(cur.fetchall())
    rows = filter(lambda x: x[1].startswith("N"), rows)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
