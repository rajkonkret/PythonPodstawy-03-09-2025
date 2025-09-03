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

