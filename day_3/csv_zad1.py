# csv - dane oddzielone znakiem podziału ,;tab
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv

# obsługa plików csv

fields = ['name', 'branch', 'year', 'coe']
row = ["Radek", "coe", "3", 90]

filename = "records.csv"

with open(filename, "w", newline="") as fh:
    csvwriter = csv.writer(fh)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

read_fields = []
read_rows = []

with open(filename, "r", newline="") as f:
    csvreader = csv.reader(f, delimiter=",")
    print(csvreader)
    # <_csv.reader object at 0x00000205B5DC26E0> iterator

    read_fields = next(csvreader)  # w czyta pierwszą linię,  ustawi odczyt na następną

    for row in csvreader:  # odczyt od drugiej lini
        read_rows.append(row)

print("Fields:", read_fields)
print("Rows:", read_rows)
# <_csv.reader object at 0x000001F02B6D2740>
# Fields: ['name', 'branch', 'year', 'coe']
# Rows: [['Radek', 'coe', '3', '90']]
print(read_rows[0][0])  # Radek
