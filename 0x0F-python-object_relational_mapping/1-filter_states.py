#!/usr/bin/python3
"""Module for listing all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    list_query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(list_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
