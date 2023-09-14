#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

connection = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database_name
)

cursor = connection.cursor()
query = """
SELECT IFNULL(GROUP_CONCAT(cities.name SEPARATOR ', '), '')
FROM cities
INNER JOIN states ON cities.state_id = states.id
WHERE states.name = %s;
"""
cursor.execute(query, (state_name,))

result = cursor.fetchone()
if result:
    cities_string = result[0]
    print(cities_string)

cursor.close()
connection.close()
