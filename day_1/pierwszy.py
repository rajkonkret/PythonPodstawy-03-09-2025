import sys

print()  # wypisz/wydrukuj
# Process finished with exit code 0 - nie ma błedów
# zasady pep8 - https://peps.python.org/pep-0008/
print()
# ctrl alt l - formatowanie kodu
print("NAzywam sie Radek")  # NAzywam sie Radek
print("NAzywam sie Radek")  # NAzywam sie Radek
print("NAzywam sie Radek")  # NAzywam sie Radek
print("NAzywam sie Radek")  # NAzywam sie Radek
print("NAzywam sie Radek")  # NAzywam sie Radek
print("NAzywam sie Radek")  # NAzywam sie Radek
# ctrl d - powielanie linii
print('Nazywam się Radek')  # Nazywam się Radek
# ctrl / - komentarz
# print("Radek')
#   File "C:\Users\CSComarch\PycharmProjects\PythonPodstawy-03-09-2025\pierwszy.py", line 14
#     print("Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 14)
# Process finished with exit code 1

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, typ tekstowy

print("39")  # str
print("39" + "39")  # konkatenacja stringów, łaczy stringi 3939

print(39)
print(type(39))  # <class 'int'>, liczby całkowite
print(39 + 39)  # 78

# print("39" + 39) # TypeError: can only concatenate str (not "int") to str

# rzutowanie - musimy jawnie rzutować typy
print(int("39") + 39)  # int() - rzutowanie na int, 78

print("39" + str(39))  # 3939, str() - rzutowanie na tekst

print(168 * 60)  # 10080
print("168" * 35)
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168

print(10 * "-")  # ----------

print(sys.int_info)

# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# zmienna - pudełko na dane, posiada nazwę
# snake_case
# nazwa zmiennej powinna podpowiadac co zawiera

# typowanie dynamiczne
# przyjmuje typ na podstawie danych
name = "Radek"
# przypisanie do zmiennej wartości Radek
print(name)
print(type(name))  # <class 'str'>

name = 90
print(name)
print(type(name))  # <class 'int'>

# podpowiedzi
name: str = "Radek"  # Tylko podpowiedz!!!
print(type(name))  # <class 'str'>

name = 90
print(type(name))  # <class 'int'>
#  pip install mypy - instalujemy w terminalu
#  cd .\day_1\ - wejście do odpowiedniego katalogu
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonPodstawy-03-09-2025> mypy .\pierwszy.py
# pierwszy.py:65: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:70: error: Name "name" already defined on line 60  [no-redef]
# pierwszy.py:73: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 3 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonPodstawy-03-09-2025>
