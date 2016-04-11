import MySQLdb

# Open database connection
db = MySQLdb.connect(host="144.126.12.11", port=3306, user="hpr", passwd="hunterdon", db="surveys")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Test
cursor.execute("SELECT * FROM test;")
data = cursor.fetchall()
for line in data:
    for val in line:
        print(val)
    print("")

# disconnect from server
db.close()