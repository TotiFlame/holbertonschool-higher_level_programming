#!/usr/bin/python3
''' task 0'''
import MySQLdb
import sys


db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()