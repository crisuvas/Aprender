import sqlite3

connection = sqlite3.connect('music.db')
consult = connection.cursor()
table = "CREATE TABLE music(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," \
        "song VARCHAR(30) NOT NULL," \
        "artist VARCHAR(30) NOT NULL," \
        "album VARCHAR(30) NOT NULL);"

if consult.execute(table):
    print("The table was created")
else:
    print("I have some syntax error")

consult.close()
connection.commit()
connection.close()
