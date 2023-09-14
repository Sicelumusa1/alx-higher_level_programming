#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

connection = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database_name
)

cursor = connection.cursor()
query = """
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;"""
cursor.execute(query)

result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
connection.close()
