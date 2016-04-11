__author__ = 'Tim'

import sys
print(sys.path)
sys.path.append('/usr/lib/python2.7/site-packages')
print(sys.path)

import pymysql

# Connect to the database
connection = pymysql.connect(host='144.126.12.11',
                             user='hpr',
                             password='hunterdon',
                             db='surveys',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# prepare a cursor object using cursor() method
cursor = connection.cursor()

# Test
cursor.execute("SELECT * FROM test;")
data = cursor.fetchall()
for line in data:
    for val in line:
        print(val)
    print("")

# disconnect from server
connection.close()


# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
#
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()
#
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()

