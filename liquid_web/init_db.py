import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('video 1', 'Content')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('video 2', 'Content')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('create video', ' ')
            )

connection.commit()
connection.close()
