#!/usr/bin/python3
""" List all states with a name starting with N from the hbtn_0e_0_usa """

import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name REGEXP '^[N].*$' ORDER BY states.id")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()
