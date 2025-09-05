class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizujaca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # pole jako prywatne, brak dostępu poza klasą
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10  # pr = pr + 10

    def licznik(self):
        print(f'Prędkość wynosi {self.__predkosc} km/h')

    def hamuj(self):
        self.__predkosc -= 25
        self.__zmien_zbieg()

    def __zmien_zbieg(self):
        print("zmiana biegu")


sam = Car("Porsche", 2025)
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
# pole prywatne
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(sam.__predkosc)  # 50
# odczyt poprzez dedykowaną metodę
sam.licznik()  # Prędkość wynosi 50 km/h
sam.__predkosc = 0  # pole publiczne inne niz pole prywatne o tej samej nazwie
sam.licznik()  # Prędkość wynosi 50 km/h
sam.hamuj()
sam.hamuj()
sam.licznik()  # Prędkość wynosi 0 km/h
# Prędkość wynosi 50 km/h
# zmiana biegu
# zmiana biegu
# Prędkość wynosi 0 km/h
