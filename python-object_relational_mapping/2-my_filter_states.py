"""
first task in Python ORM
"""

import MySQLdb
import sys

user = sys.argv[1]
passwd = sys.argv[2]
database = sys.argv[3]
arg = sys.argv[4]

db = MySQLdb.connect(user=user, passwd=passwd, database=database)

cur = db.cursor()


def main():
    """
    the main function
    """
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id;", (arg,))
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
