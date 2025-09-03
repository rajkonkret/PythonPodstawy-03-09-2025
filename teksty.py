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


