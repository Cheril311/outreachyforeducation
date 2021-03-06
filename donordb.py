import sqlite3

conn = sqlite3.connect('donorinfo.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE students (name TEXT, email TEXT, city TEXT, amount TEXT)')
print ("Table created successfully")
conn.close()