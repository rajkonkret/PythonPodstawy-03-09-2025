#  stworzyć funkcję obliczającą średnią (ocen)

def liczby(imie=None, *cyfry):
    print(cyfry)  # * - worek na dane, (1, 2, 3, 4, 5)
    count = len(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"Średnia dla ucznia: {imie} wynosi: {avg}")
    finally:
        print("Kolejny uczeń")


# wywołanie funkcji z argumentami
imie, *oceny = "Radek", 1, 2, 3, 4, 5
liczby("Radek", 1, 2, 3, 4, 5)
liczby()  # ()
liczby(1)  # (1,)
liczby("a", 1)
# (1, 2, 3, 4, 5)
# Średnia dla ucznia: Radek wynosi: 3.0
# Kolejny uczeń
# ()
# Bład: division by zero
# Kolejny uczeń
# ()
# Bład: division by zero
# Kolejny uczeń
# (1,)
# Średnia dla ucznia: a wynosi: 1.0
# Kolejny uczeń
