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
    print(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)  # [47, 33, 22, 44, 8, 18]
