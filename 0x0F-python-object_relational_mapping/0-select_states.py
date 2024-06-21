#!/usr/bin/python3
"""
Module for listing all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # SQL query to select all states, ordered by id
    list_query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(list_query)

    # Fetch and print all results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
