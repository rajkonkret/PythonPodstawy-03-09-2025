# zbiór (set) - przechowują unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# nie ma indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # tworzymy zbiór z listy
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbiór
zb2 = set()  # tworzenie pustego zbiory tylko za pomocą słowka set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie eleemntu do zbioru
# ctrl d - powielanie linii
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(24)
zbior.add(32)
zbior.add(17)
print(zbior)
# {32, 33, 66, 777, 11, 44, 17, 18, 22, 55, 24}

# usuniecie elementu ze zbioru
zbior.remove(55)
print(zbior)
# {32, 33, 66, 777, 11, 44, 17, 18, 22, 24}

# pop() - usunięcie pierwszego elementu
print(zbior.pop())  # 32
print(zbior)  # {33, 66, 777, 11, 44, 17, 18, 22, 24}
# zbior.pop().pr i tabulator

zmienna = zbior.pop()
print("Usunięty:", zmienna)  # Usunięty: 33

# operacje na zbiorach
zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}  # klamerka to oznacza zbiór
print(type(zbior_2))  # <class 'set'>
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}

# zwraca nowy zbiór
# suma zbiorów
print(zbior | zbior_2)  # {66, 777, 11, 44, 12.34, 17, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {66, 777, 11, 44, 12.34, 17, 18, 52, 22, 24, 667, 62}

# częśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica
print(zbior - zbior_2)  # {66, 777, 17, 22, 24}
print(zbior.difference(zbior_2))  # {66, 777, 17, 22, 24}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# update() - do zbioru dopisuje elementy drugiego zbioru
# zmienia bazowy !!!
zbior.update(zbior_2)
print(zbior)  # {66, 777, 11, 44, 12.34, 17, 18, 52, 22, 24, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (66, 777, 11, 44, 12.34, 17, 18, 52, 22, 24, 667, 62)

# sprawdzenie
print(777 in zbior)  # True
print(777 in lista)  # True
print(777 in krotka)  # True
print(767 in zbior)  # False
