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


insert()
