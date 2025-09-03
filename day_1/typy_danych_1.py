wiek = 47  # int
rok = 2025  # int
temp = 36.6  # float, zmiennoprzecinkowe

print(wiek + rok)  # 2072
print(wiek - rok)  # -1978
print(wiek * rok)  # 95175
print(wiek / rok)  # 0.023209876543209877

print(rok // wiek)  # 43, częśc całkowita z dzielenia
print(rok % wiek)  # modulo, reszta z dzielenia

print(10 % 3)  # restza 1

print(wiek ** rok)  # potęgowanie
# len() - długość
# str() - zmieniamy na tekst i mierzymy długość
print(len(str(wiek ** rok)))  # 3386
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits)
# for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 4 / 1 + 4 / 2)  # 36.0
print(54 - 5 * (4 / 1 + 4) / 2)  # 34.0

# float - liczby zmiennoprzecinkowe
# posiadają bład zaookrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal()  - pozwala ominąc problem zaokrąglenia

# typ logiczny
# prawda, fałsz
# True, False
# 1, 0

czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, boolean, typ logiczny

print(int(True))  # 1
print(int(False))  # 0

# bool() - rzutowanie na typ logiczny
print(bool(100))  # True
print(bool(-100))  # True
print(bool("Radek"))  # True

print(bool(""))  # False
print(bool(None))  # False, odpowiednik null, nic, nie ma, nie wiem

# and - i
print(True and False)  # False
# Expression    Evaluates to
# True and True    True
# True and False    False
# False and True    False
# False and False    False

# or - lub
# True or True    True
# True or False    True
# False or True    True
# False or False    False

print(True or False)  # True

# not - negacja
print(not True)  # False
print(not False)  # True

a = 7
b = 89
print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 7 > 89 = False
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 7 < 89 = True
print(f"Porównanie {a} >= {b} = {a >= b}")  # Porównanie 7 >= 89 = False
print(f"Porównanie {a} <= {b} = {a <= b}")  # Porównanie 7 <= 89 = True
print(f"Porównanie {a >= b =}")  # Porównanie a >= b =False
print(f"Porównanie {a} == {b} = {a == b}")  # Porównanie 7 == 89 = False, porównanie, czy równe
print(f"Porównanie {a} != {b} = {a != b}")  # Porównanie 7 != 89 = True, czy rózne?
