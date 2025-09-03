# kolekcje

# lista - przechowuje dowolną ilosc danych, dowolnego typu na raz
# zachowuje kolejnośc przy dodawaniu elementów

# pusta lista
lista = []
print(lista)  # [] - pusta lista

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie elementu na końcu listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Anna")
lista.append("Aneta")
lista.append("Aga")
lista.append("Piotr")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Aneta', 'Aga', 'Piotr']
#    0         1        2        3       4        5      6
#    -7        -6       -5       -4     -3        -2     -1
# indeksy

print(lista[1])  # Tomek
print(lista[3])  # Anna
print(lista[5])  # Aga

# print(lista[10])  # IndexError: list index out of range

print(len(lista))  # 7
print(lista[len(lista) - 1])  # Piotr
print(lista[-1])  # Piotr - ostatni element
print(lista[-2])  # Aga

# fragment listy - slicowanie
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'] -> indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Anna', 'Aneta', 'Aga', 'Piotr'], ostatni włącznie
print(lista[2:6])  # ['Zenek', 'Anna', 'Aneta', 'Aga'] bez ostatniego

print(lista[2:15])  # ['Zenek', 'Anna', 'Aneta', 'Aga', 'Piotr'] wypisze tylko te które są
print(lista[10:234])  # []

print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Anna', 'Aneta', 'Aga', 'Piotr']
print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek'], indeks 2
print(lista[::2])  # [start:stop:krok], co drugi ['Radek', 'Zenek', 'Aneta', 'Piotr']

# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Aneta', 'Aga', 'Piotr']
#    0         1        2        3       4        5      6
#    -7        -6       -5       -4     -3        -2     -1

print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # [0:5] ['Radek', 'Tomek', 'Zenek', 'Anna', 'Aneta']

lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[::2])  # [0, 2, 4, 6, 8, 10, 12, 14]

# w odwrotnej kolejności
print(lista_15[::-1])  # [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] krok -1

# nadpisanie elementu
lista[3] = "Radek"
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Radek', 'Aneta', 'Aga', 'Piotr']

# dopisanie eleemntu do listy we wskazanym miejscu (indeksie)
lista.insert(1, "Roman")
print(lista)
# ['Radek', 'Roman', 'Tomek', 'Zenek', 'Radek', 'Aneta', 'Aga', 'Piotr']

# sprawdzenie indexu dla eleemntu
print(lista.index("Radek"))  # 0, pierwszy napotkany

print(lista.count("Radek"))  # występuje 2 razy

# usunięcie elementu, pierwszy napotkany
lista.remove("Radek")
print(lista)

# usunięcie po indeksie, zwraca usunięty element
print(lista.pop(5))  # Aga
print(lista)  # ['Roman', 'Tomek', 'Zenek', 'Radek', 'Aneta', 'Piotr']
print(lista.pop())  # Piotr - usunie ostatni
