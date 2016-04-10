import MySQLdb

db = MySQLdb.connect("localhost", "monitor", "password", "temps")
curs=db.cursor()