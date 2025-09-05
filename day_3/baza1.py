# baza danych - system przechowywania danych
# sql, nosql
import sqlite3

# baza danych w jednym pliku lub pamięci

sql_connection = None

try:
    sql_connection = sqlite3.connect("baza.db")
    cursor = sql_connection.cursor()
    print('Baza została podłączona')

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    salary REAL NOT NULL);
    """

    # cursor.execute(query)
    # sql_connection.commit()

    insert = """
    INSERT INTO developers(id,name,salary) VALUES (1, 'Radek', 10000);
    """
    # cursor.execute(insert)
    # sql_connection.commit()

    select = """
    SELECT * FROM developers;
    """
    for row in cursor.execute(select):
        print(row)  # (1, 'Radek', 10000.0)

except sqlite3.Error as e:
    print("Błąd:", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")
