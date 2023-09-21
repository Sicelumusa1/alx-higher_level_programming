#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves a comma-separated
string of cities belonging to a specified state
"""

import MySQLdb
import sys

if __name__ == "__main__":

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    #  Establish a connection to the MySQL database
    connection = MySQLdb.connect(host="localhost", port=3306, user=username,
                                 passwd=password, db=database_name)

    #  Create a cursor and interact with the database
    cursor = connection.cursor()
    query = """
    SELECT IFNULL(GROUP_CONCAT(cities.name SEPARATOR ', '), '')
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s;
    """
    cursor.execute(query, (state_name,))

    #  Fetch and display results
    result = cursor.fetchone()
    if result:
        cities_string = result[0]
        print(cities_string)

    #  Free resources
    cursor.close()
    connection.close()
