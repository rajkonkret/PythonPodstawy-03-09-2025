# działania z plikami
# filehandler - rura do pliku
# context manager - pomaga w pracy z plikami
# with - context manager w pythonie

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log", "w", encoding="utf-8") as fh:  # fh - filehandler
    fh.write("Powitanie\n")
    fh.write("kolejna\n")
    fh.write("jescze jedno\n")
    fh.write("Radek Kowalski")

# FileExistsError: [Errno 17] File exists: 'test.log'
# with open('test.log', "x", encoding="utf-8") as f:
#     f.write("Powitanie")

# encoding="utf-8" -kodowanie znaków
with open("test.log", "w", encoding="utf-8") as file:
    file.write("Nowa Zawartość\n")

with open("test.log", "a", encoding="utf-8") as f:
    f.write("Dopisanie do istniejącego pliku\n")

with open("test.log", "r", encoding="utf-8") as file:
    lines = file.read()

print(lines)
# Nowa Zawartość
# Dopisanie do istniejącego pliku
