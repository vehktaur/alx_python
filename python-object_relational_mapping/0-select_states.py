"""
first task in Python ORM
"""

import MySQLdb

db = MySQLdb.connect(host = "localhost", user = "watashi", passwd =  "passwd")

cur = db.cursor()

cur.execute("USE hbtn_0e_0_usa; SELECT * FROM states ORDER_BY id;" )