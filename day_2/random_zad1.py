import random

# operacje na liczbach (pseudo)losowych

"""Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # int od 1 to 100

print(random.randrange(1, 100))  # int, od 1 do 99
print(random.randrange(5))  # int, od 0 do 4

print(random.random())  # 0.4380295884776525, float od 0 do 0.99999999
print(random.random() * 8)  # 3.976108553567135, float od 0 do 7.99999999

lista = [67, 45, 32, 68, 69, 90, 42]
print(random.choice(lista))  # elelement z kolekcji 67

lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)

wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # [20, 31, 31, 11, 19, 29] z powtórzeniami
print(random.sample(lista_kule, k=6))  # bez powtórzeń, [35, 15, 18, 29, 11, 1]
print(random.sample(lista_kule, 6))  # bez powtórzeń, [42, 1, 37, 31, 3, 17]
