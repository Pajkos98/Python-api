import sqlite3

con = sqlite3.connect("tanulok.db")
print("Adatbázis elindult")

con.execute(
    "create table students (id INTEGER PRIMARY KEY AUTOINCREMENT, keresztnev TEXT NOT NULL, vezeteknev TEXT UNIQUE NOT NULL, lakcim TEXT NOT NULL, Osztaly TEXT NOT NULL, Igazolvanyszam TEXT NOT NULL)")

print("Tábla létrehozva")

con.close()
