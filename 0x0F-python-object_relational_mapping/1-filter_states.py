#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves States records
where thr name starts with'N'.
"""


import MySQLdb
import sys


if __name__ == "__main__":

    #  Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    #  Establish a database connection
    connection = MySQLdb.connect(host="localhost", port=3306, user=username,
                                 passwd=password, db=database_name)

    #  Create a cursor object to interact with the database
    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%';"
    cursor.execute(query)

    #  Display results
    result = cursor.fetchall()
    for row in result:
        print(row)

    #  Free resources
    cursor.close()
    connection.close()
