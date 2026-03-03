from search import search_movie
import sqlite3

while True:  # This loops makes the data entry easier, instead of loading the script manually every time.
    database = 'pmdb.db'

    title = input("What movie would you like to search? ")
    results = search_movie(title)[:2]


    for i, movie in enumerate(results): # Basic loop statement, going through the results from TMDB and highlighting the top two (as most relevant results might be in the top two)
        print(i+1,movie["title"], movie["release_date"],movie["original_language"]) # basic print statement laying out the headers we want extracted

    ans = input("Which one is correct? ")
    results = results[int(ans) - 1]  # This adjustment fixes the off by one error
    print("Ok, got it")

    format = input("What format is it? ")

    with sqlite3.connect(database, timeout=10) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO movies (title,release_date,original_language, format)
             VALUES (?, ?, ?, ?)''', (results["title"],results["release_date"],results["original_language"], format))
            conn.commit()

    anyelse = input("anything else? ")
    if anyelse == "no":
        break