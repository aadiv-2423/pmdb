import sqlite3

database = 'pmdb.db'

try:

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
        
      id INTEGER PRIMARY KEY,
      title text NOT NULL,
      release_date INTEGER,
      original_language text,
      format text)''')
        conn.commit()

except sqlite3.OperationalError as e:
    print(e)

# simple try/except to create the table, populate it with the required fields and print and error message if SQLite3 has an error.