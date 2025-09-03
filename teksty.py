tekst = "Witaj Świecie"

print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
tekst.upper()
print(tekst)  # Witaj Świecie
#    """ Return a copy of the string converted to uppercase. """ - zwraca kopie
print(tekst.upper())  # WITAJ ŚWIECIE
upper_case = tekst.upper()
print(upper_case)

print(tekst.capitalize())  # Witaj świecie
print(tekst.lower())  # witaj świecie

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunie wiądace i końcowe spacje i białe znaki
print(tekst.removeprefix("Witaj").strip())  # "Świecie"

encoded_s = tekst.encode("utf-8")
print(encoded_s)  # b'Witaj \xc5\x9awiecie'
# b - typ bajtowy
print(type(encoded_s))  # <class 'bytes'>
# \xc5\x9a - kod szesnastkowy znaku Ś
print(encoded_s.decode("utf-8"))  # Witaj Świecie

print(tekst)
# Witaj Świecie
# 0123456789....  - indeksujemy od 0

print(tekst[4])  # "j" indeks 4, pozycja 5

print(tekst.count("i"))  # wytsępuje 3 razy
# x:, __start:, __end: nie przepisujemy!
print(tekst.count("j", 0, 4))  # 0 wystąpień, indeksy 0123

imie = 'Radek'
print(imie)  # Radek
print("Imie:", imie)  # Imie: Radek

starszy = "Witaj %s!"  # %s - wstaw w to miejsce str -> %s str
print(starszy % imie)  # Witaj Radek!

# f - string
tekst_format = f"Mam na imię {imie} i lubię pythona."
print(tekst_format)  # Mam na imię Radek i lubię pythona.

tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# "	 Mam na imię Radek
#  i lubię pythona"
# \t - tab
# \n - nowa linia
# \b - backspace

print("Witaj {} {}".format(imie, "Tomek"))  # Witaj Radek, Witaj Radek Tomek

print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

# komentarz dokumentacyjny
"""Komentarz
wielolinijkowy"""
