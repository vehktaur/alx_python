"""
first task in Python ORM
"""

import MySQLdb

db = MySQLdb.connect(host = "localhost", user = "watashi", passwd =  "passwd", database = "hbtn_0e_0_usa")

cur = db.cursor()

cur.execute("SELECT * FROM states ORDER_BY id" )