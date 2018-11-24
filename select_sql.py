import sqlite3


def select():
    db2 = sqlite3.connect('books.db')
    print("You are in the select section")
    db2.row_factory = sqlite3.Row
    consult = db2.cursor()
    consult.execute("SELECT * FROM books;")
    rows = consult.fetchall()
    list_row = []
    for row in rows:
        s = {'name': row['name'],
             'author': row['author'],
             'year': str(row['year'])
             }
        list_row.append(s)
    consult.close()
    db2.close()
    return list_row


print(select())

