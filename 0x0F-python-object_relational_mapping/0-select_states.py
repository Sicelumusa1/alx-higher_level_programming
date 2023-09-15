#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieve a list of states
"""

import MySQLdb
import sys


if __name__ == "__main__":
    
    #  Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    #  Establish a connection to the MySQL database
    connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    #  Create a cursor object to interact with the database
    #  get required records and execute the query
    cursor = connection.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC;"
    cursor.execute(query)

    #  Fetch  and display the results
    result = cursor.fetchall()
    for row in result:
        print(row)

    # free resources
    cursor.close()
    connection.close()
