import sqlite3


def insert():
    db = sqlite3.connect('music.db')
    print("I'm in the insert section")
    song = input("What is the song?\n")
    artist = input("Who is the artist?\n")
    album = input("Which is the album?\n")

    consult = db.cursor()
    str_consult = "INSERT INTO music(song, artist, album) VALUES" \
                  "('" + song + "','" + artist + "','" + album + "');"
    print(str_consult)
    consult.execute(str_consult)
    consult.close()
    db.commit()
    db.close()


def select():
    db = sqlite3.connect('music.db')
    print("You are in the select section")
    db.row_factory = sqlite3.Row
    consult = db.cursor()
    consult.execute("SELECT * FROM music;")
    rows = consult.fetchall()
    list_row = []
    for row in rows:
        s = {'id': row['Id'],
             'song': row['song'],
             'artist': row['artist'],
             'album': row['album']
             }
        list_row.append(s)
    consult.close()
    db.close()
    return list_row


def menu():
    option = int(input("Select one of the next options.\n1)Insert\n2)Select\n"))
    if option == 1:
        insert()
        menu()
    elif option == 2:
        novel_list = select()
        for novel in novel_list:
            print(novel['id'], novel['song'], novel['artist'], novel['album'])
        menu()
    else:
        print("Option no valid")
        menu()


menu()
