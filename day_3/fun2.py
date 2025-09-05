a = 10  # globalny scope
b = 10


def dodaj():
    a = 7  # przyjmie to jako zmienne lokalne, nie zmimeni wartości zmiennej globalnej o tej samej nazwie
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # uzyje globalne


def dodaj3():
    global a
    a = 9  # nadpisze wartość globalnego a
    b = 90
    print(a + b)


print(f"Wartość a z góry: {a}")  # Wartość a z góry: 10
dodaj()  # 15
print(f"Wartość a z góry: {a}")  # Wartość a z góry: 10
dodaj2()  # 20
print(f"Wartość a z góry: {a}")  # Wartość a z góry: 10
dodaj3()  # 99
print(f"Wartość a z góry: {a}")  # Wartość a z góry: 9
dodaj2()  # 19
