# baza danych - system przechowywania danych
# sql, nosql
import sqlite3

# baza danych w jednym pliku lub pamięci

sql_connection = None

try:
    sql_connection = sqlite3.connect("baza.db")
    cursor = sql_connection.cursor()
    print('Baza została podłączona')

except sqlite3.Error as e:
    print("Błąd:", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")
