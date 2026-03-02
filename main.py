from search import search_movie
import sqlite3

title = input("What movie would you like to search? ")
results = search_movie(title)[:2]


for i, movie in enumerate(results): # Basic loop statement, going through the results from TMDB and highlighting the top two (as most relevant results might be in the top two)
    print(i+1,movie["title"], movie["release_date"]) # basic print statement laying out the two headers we want extracted

ans = input("Which one is correct? ")
results = results[int(ans)]
print("Ok, got it")

# index search results and tie in SQL INSERT INTO func