#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    state = sys.argv[4]
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name FROM cities INNER JOIN states ON\
          states.id = state_id WHERE states.name = %s ORDER BY cities.id ASC;"
    cursor.execute(query, (state,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
