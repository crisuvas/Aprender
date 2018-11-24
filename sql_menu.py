import sqlite3


def insert():
    db1 = sqlite3.connect('books.db')
    print("You are in the insert function")
    name1 = str(input("Write the title of your novel\n"))
    author1 = str(input("Write the author of the novel\n"))
    year1 = str(input("Write the year of the novel\n"))

    consult = db1.cursor()
    str_consult = "INSERT INTO books(name, author, year) VALUES" \
                  "('"+name1+"','"+author1+"',"+year1+");"
    print(str_consult)
    consult.execute(str_consult)
    consult.close()
    db1.commit()
    db1.close()


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


def menu():
    option = int(input("Choose an option:\n1)Insert\n2)Select\n"))
    if option == 1:
        insert()
        menu()
    elif option == 2:
        novel_list = select()
        for novel in novel_list:
            print(novel['name'], novel['author'], novel['year'])
        menu()
    else:
        print("Option no valid")
        menu()


menu()
