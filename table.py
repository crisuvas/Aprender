import sqlite3

connection = sqlite3.connect('books.db')
consult = connection.cursor()
table = "CREATE TABLE books(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," \
        "name VARCHAR(30) NOT NULL," \
        "author VARCHAR(40) NOT NULL," \
        "year INTEGER(9) NOT NULL);"

print(table)

if consult.execute(table):
    print("The table was created")
else:
    print("The table was not created")

consult.close()
connection.commit()
connection.close()
