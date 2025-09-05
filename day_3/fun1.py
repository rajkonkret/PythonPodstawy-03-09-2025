# funkcja - wydzielony fragment kodu, można wywołać w dowolnym momencie
# funkcja musi byc najpierw zaddekalrowana
# zeby uruchomic funkcję musi zostać wywołana

a = 8
b = 9


# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # funkcja z argumnetami a i b
    print(a + b)  # lokalne zmienne a i b


def odejmij(a, b, c=0):  # c=0 argument o wartości domyślnej
    print(a - b - c)


# argumenty po pozycji
# wywołanie funkcji
dodaj()  # 17
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 90)  # 95

odejmij(1, 2, 3)  # -4
odejmij(1, 2)  # -1

# argumenty po nazwie
odejmij(c=9, b=9, a=8)  # -10

# mieszane
# pozycyjne przed nazwanymi!
odejmij(1, c=9, b=7)  # -15


# odejmij(c=9, 1, 4) # SyntaxError: positional argument follows keyword argument


# print(dodaj() + dodaj2(5, 6))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

# funkcja zwracająca wynik
def dodaj3():
    return a + b  # zwróć


def odejmij2(a=0, b=0, c=0):
    return a - b - c


print(dodaj3())  # 17
zm = odejmij2(4, 5, 6)
print(zm)  # -7
print(dodaj3() + dodaj3())  # 34
