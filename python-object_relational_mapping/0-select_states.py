#!/usr/bin/python3
""" List all states from the database hbtn_0e_0_usa  """

import MySQLdb
from MySQLdb.constants import FIELD_TYPE
from sys import argv


if __name__ == "__main__":
    my_conv = { FIELD_TYPE.LONG: int}
    db = MySQLdb.connect(host="localhost", port="3306", user=argv[1], 
		    passwd=argv[2], db=argv[3], conv=my_conv)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()
