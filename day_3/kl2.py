class Human:
    """
       Klasa Human opisująca człowieka w pythonie
    """

    # pod self podstawia zmienna przechowująca dany oiekt np.: cz1
    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")  # cz1.imie

    def wypisz_wiek(self):
        print(f'Mama {self.wiek} lat.')

# TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
# cz1 = Human()

cz1 = Human("Radek", 45, 170, "m")
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
# Radek
# 45
# 170
# m
cz1.powitanie()  # Nazywam się Radek

cz2 = Human("Anna", 34, 170)
print(cz2.imie)
print(cz2.wiek)
print(cz2.wzrost)
print(cz2.plec)
# Anna
# 34
# 170
# k
cz2.wypisz_wiek() # Mama 34 lat.