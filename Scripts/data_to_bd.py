import sqlite3
import csv

con = sqlite3.connect('../baseDB.db')
cur = con.cursor()

with open('../Data/data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f.readlines()[1:], delimiter=',', quotechar='"')
    data = [i for i in reader]

for id, name, genres, themes, years, orig_name, description in data:
    cur.execute(
        "INSERT INTO anime(title, genres_id, themes_id, years_id, orig_name, description) VALUES(?, ?, ?, ?, ?, ?)",
        (name, genres, themes, years, orig_name, description))

with open('../Data/years.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f.readlines()[1:], delimiter=',', quotechar='"')
    data = [i for i in reader]

for year, id in data:
    cur.execute("INSERT INTO years(year) VALUES(?)", (year,))

with open('../Data/genres.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f.readlines()[1:], delimiter=',', quotechar='"')
    data = [i for i in reader]

for genre, id in data:
    cur.execute("INSERT INTO genres(title) VALUES(?)", (genre,))

with open('../Data/themes.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f.readlines()[1:], delimiter=',', quotechar='"')
    data = [i for i in reader]

for theme, id in data:
    cur.execute("INSERT INTO themes(title) VALUES(?)", (theme,))

con.commit()
