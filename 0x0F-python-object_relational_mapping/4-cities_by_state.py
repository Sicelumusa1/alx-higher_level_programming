#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves information about
cities and their respective states, ordering the results by city id
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

    #  Create a cursor object and interact with dadabase
    cursor = connection.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;"""
    cursor.execute(query)

    #  Fetch and display results
    result = cursor.fetchall()
    for row in result:
        print(row)

    #  Free resources
    cursor.close()
    connection.close()
