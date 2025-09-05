# klasy - element programowania obiektowego
# klasa - szablon, przepis, opis
# obiekt - instancja klasy - stworzny z przepisu
# klasa musi byc zadeklarowana przed uzyciem
# tworzenie obiektu uruchamia metode inicjalizujacą
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase - UpperCamelCase
# deklaracja klasy
class Human:
    """
    Klasa Human w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"


print(Human.__doc__)  #
# Klasa Human w Pythonie
#  cd .. wyjscie wyzej
# cd .\day_3\ - wejscie do wskazanego katalogu
# pydoc -b - serwer dokumentacji
#  pydoc -w kl1 - dokumentacja w formie html

# obiekt z klasy
cz1 = Human()
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# #
# None
# k
cz1.imie = "Radek"
cz1.wiek = 34
cz1.plec = "m"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Radek
# 34
# m
cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 45
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Anna
# 45
# k
