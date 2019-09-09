# create db an insert data


import sqlite3

conn = sqlite3.connect('testnet.db')
cur = conn.cursor()


def createdb():
    cur.execute("""CREATE TABLE IF NOT EXISTS testnet(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME STR NOT NULL,
                PHONE STR NOT NULL,
                SURNAME STR NOT NULL)""")
    conn.commit()
    print('db created ')
    insert123()

def insert123():
    tname = input('what is your name? ').upper()
    tphone = input('Enter phone number? ').capitalize()
    tsurname = input('enter surname: ').upper()
    cur.execute("INSERT INTO testnet(NAME, PHONE, SURNAME)VALUES(?,?,?)", (tname, tphone,tsurname))
    conn.commit()
    cur.close()
    print('done')



createdb()