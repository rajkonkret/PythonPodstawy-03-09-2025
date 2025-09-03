# krotka, tupla - do odczytu, niemutowalna kolekcja
# pozwala efektywniej zarządzac pamięcią
# stała - zmienna niezmienna

tupla_imona = ("Radek", "Tomek", "Zenek", "Ela")
print(tupla_imona)  # ('Radek', 'Tomek', 'Zenek', 'Ela')
print(type(tupla_imona))  # <class 'tuple'>

tupla_liczba = 43, 55, 22.34, 11, 200
print(type(tupla_liczba))  # <class 'tuple'>
print(tupla_liczba)  # (43, 55, 22.34, 11, 200)

tupla = (43)
print(type(tupla))

tupla2 = 43,
print(type(tupla2))  # <class 'tuple'>
print(tupla2)  # (43,)

# PEP8 zaleca by tuple jednoelementowe robić z nawiasami
tupla3 = ("Radek",)
print(type(tupla3))  # <class 'tuple'>
print(tupla3)  # ('Radek',)

# tupla jest niemutowalna
# TypeError: 'tuple' object does not support item assignment
# tupla_liczba[3] = 123

del tupla_liczba  # skasowanie całej tupli
# print(tupla_liczba) # NameError: name 'tupla_liczba' is not defined. Did you mean: 'tupla_imona'?

print(tupla_imona.index("Radek"))  # index 0
print(tupla_imona.count("Radek"))  # wystepuje 1 raz

tup = 1, 2
print(type(tup))  # <class 'tuple'>
a, b = 1, 2
print(a, b)

# rozpakowanie tupli
a, b = tup
print(a, b)  # 1 2

tup2 = 1, 2, 3
# a, b = tup2  # ValueError: too many values to unpack (expected 2)
a, *b = tup2  # * worek na pozostałe dane
print(a, b)  # 1 [2, 3]

print(tupla_imona)  # ('Radek', 'Tomek', 'Zenek', 'Ela')
# name1, name2, name3

name1, name2, *name3 = tupla_imona
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Ela']

name1, *name2, name3 = tupla_imona
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek'] Ela

*name1, name2, name3 = tupla_imona
print(name1, name2, name3)  # ['Radek', 'Tomek'] Zenek Ela

# zwróci posortowaną listę
print(sorted(tupla_imona))
# ['Ela', 'Radek', 'Tomek', 'Zenek']
print(tupla_imona)  # ('Radek', 'Tomek', 'Zenek', 'Ela') krotka się nie zmieni, jest niemutowalna

lista_z_tupli = list(tupla_imona)
print(lista_z_tupli)  # ['Radek', 'Tomek', 'Zenek', 'Ela']
print(type(lista_z_tupli))  # <class 'list'>
