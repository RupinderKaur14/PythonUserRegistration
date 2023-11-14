import sqlite3

connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Registered_User (id INTEGER PRIMARY KEY, username VARCHAR(100), hashedpassword VARCHAR(100))')


query = "SELECT * FROM Registered_User"
cursor.execute(query)
data = cursor.fetchall()
print("user:", data)