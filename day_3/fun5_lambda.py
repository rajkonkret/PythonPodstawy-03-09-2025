# funkcja lambda
# skrócona forma funkcja
# return

def odejmij(a, b):
    return a - b


print(odejmij(6, 8))  # -2

odejmij2 = lambda a, b: a - b
print(odejmij2(6, 8))  # -2

# lambda zawsze ma return
wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(10))
print(wiek(18))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 4, 35, 55, 60, 100, 500]
l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 8, 70, 110, 120, 200, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 8, 70, 110, 120, 200, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 6, 8, 70, 110, 120, 200, 1000]

# map() - bierze kolejne elementy i wykonuje na nich zadaną funkcję
# funkcja wyższego rzędu - jako argument przyjmuje inna funkcje
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 70, 110, 120, 200, 1000]

# lambda jako funkcja anonimowa - nie ma nazwy
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 70, 110, 120, 200, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 8, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 2.5, lista))}")
# Zastosowanie map(): [4, 8, 12, 16, 140, 220, 240, 400, 2000]
# Zastosowanie map(): [8, 16, 24, 32, 280, 440, 480, 800, 4000]
# Zastosowanie map(): [2.5, 5.0, 7.5, 10.0, 87.5, 137.5, 150.0, 250.0, 1250.0]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 5:
        l3.append(i)
print(l3)  # [1, 2, 3, 4]

# filter()
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 5, lista))}")  # Zastosowanie filter(): [1, 2, 3, 4]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 4 and x < 100, lista))}")
# Zastosowanie filter(): [35, 55, 60]
print(f"Zastosowanie filter(): {list(filter(lambda x: 4 < x < 100, lista))}")  # Zastosowanie filter(): [35, 55, 60]
