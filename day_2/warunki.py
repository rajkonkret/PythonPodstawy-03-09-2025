# instrukcje warunkowe
# instrukcje sterowanie przepływem programu
# if
# w zależności od warunku (True/False) wykona odpowiedni blok programu

# debugger
# pułapka
odp = True
# odp = False
if odp:
    # blok programu wykonywany gdy warunek True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza cześć programu")
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Dalsza cześć programu

odp = "Radek"
if odp:  # bo bool(odp) -> True
    print("Radek")  # Radek

if odp == "Radek":  # czy konkretnie ma wartość Radek
    print("Nadal Radek")  # == porównanie

odp = 0
if odp:
    print("Działa")
else:  # w przeciwnym przypadku
    print("Zero -> False")  # Zero -> False

a = "Radek"
if len(a) > 3:
    print(f'Długość wynosi {len(a)}, więcej niz 3')

a = "Radek"
n = len(a)
if n > 3:
    print(f'Długość wynosi {n}, więcej niz 3')
# Długość wynosi 5, więcej niz 3

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f'Długość wynosi {n}, więcej niz 3')
