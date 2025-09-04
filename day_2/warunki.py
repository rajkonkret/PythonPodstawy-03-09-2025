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

# snake_case

# kolejnosc ma znaczenie
# pierwszy True powoduje wyjście z drzewka

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 40000:  # zarobki >= 10000 and zarobki < 40000
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# # # nigdy by nie weszło w ten fragment warunku
# # elif zarobki < 40000:  # zarobki >= 10000 and zarobki < 40000
# #     podatek = 0.2
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki} pln.")
# # podatek 0.2 dla przedziału 10000 do 39999


suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print("Rabat wynosi:", rabat)

rabat = 25 if suma_zam > 100 else 0  # operator warunkowy
print("Rabat wynosi:", rabat)

# napisac test z
# trzy pytania
# zliczanie punktów

# punkty = 0
# odp = input("podaj date Chrztu Polski")
# if odp == '966':
#     print("Dobrze")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Musisz poczytać")
# print("Punkty:", punkty)

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

alert_system = "email"
# alert_system = "console"
error_level = 'error'
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error_level == "error":
        lista_b.append("Krytyczny")
    elif error_level == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny bład")
else:
    print("Inny system")

print(lista_b)
# Stało się coś strasznego
# []
# System email
# ['Krytyczny']
