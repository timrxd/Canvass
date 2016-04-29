__author__ = 'Tim'

import pymysql

# Connect to the database
connection = pymysql.connect(host='cs-database.cs.loyola.edu',
                                  user='tjdowd',
                                  password='1638385',
                                  db='tjdowd',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)


# prepare a cursor object using cursor() method
cursor = connection.cursor()

# Test
cursor.execute("SELECT * FROM fake;")
data = cursor.fetchall()
print(data)
for line in data:
    for val in line:
        print(val, line[val])
    print("")

# disconnect from server
connection.close()
