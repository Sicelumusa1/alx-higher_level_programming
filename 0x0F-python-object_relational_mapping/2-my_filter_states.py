#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves State records
with a specific name provided as a command-line argument
"""

import MySQLdb
import sys


if __name__ == "__main__":

    #  Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    #  Establish a database connection
    connection = MySQLdb.connect(host="localhost", port=3306, user=username,
                                 passwd=password, db=database_name)

    #  Create a cursor object and interact with the database
    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;"
    cursor.execute(query)

    #  Fetch and display results
    result = cursor.fetchall()
    for row in result:
        print(row)

    #  Free resources
    cursor.close()
    connection.close()
