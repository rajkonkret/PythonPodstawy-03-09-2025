# pętla - mozłiwość wykonania wielokrotnie fragmentu kodu
# for - pętla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(5):
    pass  # nic nie rób

for _ in range(3):  # niema zmienna
    print('Test podłoga')
    # print(_)

for i in range(10):  # od 0 do 9
    print(i * 2)
    print(i + 2)

lista_kule = list(range(1, 50))  # od 1 do 49
lista_wynik = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)  # [47, 33, 22, 44, 8, 18]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:  # pobiera po kolei wszystkie eleemnty z lista3
    if c > 4:
        print(c, "Większe od 4")
    elif c == 4:
        print(c, "Rowne 4")
    else:
        print(c, "Mniejsze od 4")
# 0 Mniejsze od 4
# 2 Mniejsze od 4
# 4 Rowne 4
# 6 Większe od 4
# 8 Większe od 4

for i in range(0, 10, 2):  # start, stop, krok od 0 do 9 co 2
    print(i)
# 0
# 2
# 4
# 6
# 8

for i in range(-10, 0):
    print(i)

# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

for i in range(10, 0, -3):
    print(i)
# 10
# 7
# 4
# 1

for c in lista3:
    if c == 2:
        c += 1
        print(c)
    print("Za każdym przejściem pętli")

# Za każdym przejściem pętli
# 3
# Za każdym przejściem pętli
# Za każdym przejściem pętli
# Za każdym przejściem pętli
# Za każdym przejściem pętli

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
print(imiona)
print(type(imiona))  # <class 'list'>

for p in imiona:  # iteracja po kolekcji, pod p zostanie podstawiony  kolejny element kolekcji
    print(p)

# Radek
# Tomek
# Zenek
# Ania

# 0 Radek
for i in range(len(imiona)):
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - numeruje kolekcje i zwraca numer i element kolekcji
for i in enumerate(imiona):
    print(i)
# (0, 'Radek') # powstałą krotka
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')

for i, o in enumerate(imiona):  # i, o - rozpakowanie krotki
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, o in enumerate(imiona, start=1):  # i, o - rozpakowanie krotki, start - rozpoczyna od tej wartości numerowac
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
# imiona = ["Radek", "Tomek", "Zenek", "Ania", "Aga"]
wiek = [45, 65, 34, 20]

# Radek 45
for p in imiona:
    print(p, wiek[imiona.index(p)])
# 3 dla różnej długości list błąd: IndexError: list index out of range
imiona = ["Radek", "Tomek", "Zenek", "Ania", "Aga"]
# zip() - łączenie kolekcji
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 45)
# ('Tomek', 65)
# ('Zenek', 34)
# ('Ania', 20)

# i, w = ('Ania', 20)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 45
# Tomek 65
# Zenek 34
# Ania 20

print(zip(imiona, wiek))  # <zip object at 0x00000181204D56C0> iterator, generator

# 0 Radek 45
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 45))
# (1, ('Tomek', 65))
# (2, ('Zenek', 34))
# (3, ('Ania', 20))
# i, o, w = (3, ('Ania', 20))
a, b = (3, ('Ania', 20))
print(a, b)  # 3 ('Ania', 20)
c, d = ('Ania', 20)
print(c, d)
a, (c, d) = (3, ('Ania', 20))
print(a, c, d)  # 3 Ania 20
for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 45
# 1 Tomek 65
# 2 Zenek 34
# 3 Ania 20
