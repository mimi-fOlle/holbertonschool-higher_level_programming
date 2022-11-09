#!/usr/bin/python3
'''
    Take in the name of a state as an argument and list all cities of
    that state, using the database hbtn_0e_4_usa
'''
import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name LIKE BINARY '{}' "
                "ORDER BY cities.id".format(argv[4]))
    query_rows = cur.fetchall()

    for rows in query_rows:
        print(rows)
    cur.close()
    db.close()
