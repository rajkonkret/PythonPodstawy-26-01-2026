# baza danych - system przechowywania danych
# silnik - mechanizm zarządzania danymi w bazie
# bazy relacyjne, nierelacyjne
# sql, nosql
# mysql, postgress, mssql, oracle, sqlite

import sqlite3

try:
    conn = sqlite3.connect("baza_danych.db")
    c = conn.cursor()
    print("Baza danych została podłączona")

    query = """
    CREATE TABLE IF NOT EXISTS developers
    (id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAL NOT NULL);
            """
    c.execute(query)
    conn.commit()

except sqlite3.Error as e:
    print("Bład podłączania z bazą:", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza danych została podłączona
# Połączenie zostało zamknięte