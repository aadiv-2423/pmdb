import sqlite3

database = 'pmdb.db'

try:

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
      
      id INTEGER PRIMARY KEY,
      title text NOT NULL,
      year INTEGER,
      language text,
      genre text,
      format text)''')
        conn.commit()

except sqlite3.OperationalError as e:
    print(e)

# Next Steps - link TMDB API and start pulling data to track .db logic
