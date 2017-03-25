
import sqlite3

conn = sqlite3.connect('music2.db') #makes a connection to the database stored in the 
#file music.sqlite3 in the current directory, if file doesn't exist, it's created
cur = conn.cursor() #cursor is like a file handle that we can se to perform operations on the data stored in the datanase/ calling cursor() is smilar to calling open() for text files

# Make sure we can run this over and over
cur.execute('DROP TABLE IF EXISTS Tracks') 

table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'Tracks (id INTEGER PRIMARY KEY, '
table_spec += 'title TEXT, artist INTEGER, album TEXT, plays INTEGER)'
cur.execute(table_spec)

table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'Artists (id INTEGER PRIMARY KEY, '
table_spec += 'name TEXT)'
cur.execute(table_spec)


statement = 'DELETE FROM Tracks'
cur.execute(statement)
statement = 'DELETE FROM Artists'
cur.execute(statement)
conn.commit()


artists = [
        (None, 'The Clash'),
        (None, 'The Sex Pistols'),
        (None, 'The Ramones'),
        (None, 'Lcur.execute(statement, t)')
]
statement = 'INSERT INTO Artists VALUES (?, ?)'

for a in artists:
        cur.execute(statement, a)
conn.commit()

tracks = [
        (None,'London Calling', 'The Clash', 'London Calling', 235),
        (None,'Anarchy in the UK', 'The Sex Pistols', 'Never Mind the Bollocks', 144),
        (None,'Blitzkrieg Bop', 'The Ramones', 'The Ramones', 89),
        (None, 'Stairway to Heaven', 'Led Zeppelin', 'Led Zeppelin IV', 74),
]
statement = 'INSERT INTO Tracks VALUES (?, ?, ?, ?, ?)'

for t in tracks:
    cur.execute(statement, t)

conn.commit()

# Write a query to get some data out and then fetch it all into a list...
query = "SELECT artist from Tracks"
cur.execute(query)


print("\nBelow, results of a query:\n")

query = "SELECT title FROM Tracks WHERE artist='Led Zeppelin'"

# execute the query...
cur.execute(query)

# Fetch it all:
result_one = cur.fetchone()
print(result_one)

print("\nBelow, results of another query:\n")
# Another query:
q2 = "SELECT * from Tracks WHERE instr(artist, 'The')"
cur.execute(q2)
result = cur.fetchall()

for tup in result:
    print(tup)

conn.close() # Close connection to the database, we're done for now  