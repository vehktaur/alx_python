"""
first task in Python ORM
"""

import MySQLdb

db = MySQLdb.connect(host = "localhost", user = "watashi", passwd =  "passwd", database = "hbtn_0e_0_usa")

cur = db.cursor()

def main():
    query = "SELECT * FROM states ORDER BY id;"
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)
    
    
if __name__ == "__main__":
    main()

