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
query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
cursor.execute(query, (state_name,))

result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
connection.close()
