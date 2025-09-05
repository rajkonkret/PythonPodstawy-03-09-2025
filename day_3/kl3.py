from abc import ABC, abstractmethod


# ABC - pakiet to oznaczanai kals jako abstarkcyjne
# klasa abstrakcyjna musi posiadac metode abstrakcyjną
# nie da się stworzyc obiektu kalsy abstrakcyjnej
class Ptak(ABC):
    """
    Klasa Ptak
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """

        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # oznaczenie metody jako abstrakcyjna
    def wydaj_odglos(self):
        pass  # nic nie robi


class Kura(Ptak):
    """
    Dziedziczy po kalsie Ptak
    """

    def __init__(self, gatunek):
        # obowiązkowo musimy wywołąć konstrukotor z kalsy nadrzędnej
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko ko")


class Orzel(Ptak):
    """
    Dziedziczy po klasie Ptak
    """

    def wydaj_odglos(self):
        print("kier kir kier kier")

    def polowanie(self):
        print("Tu", self.gatunek, "rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Klasa Sowa dziedziczy po Ptak
    """


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 45)
# print(or1.gatunek)
# or1.latam()  # Tu Orzeł Lecę z szybkością 45
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("kura")
kur2.latam()  # Tu kura Ja nie latam
kur2.wydaj_odglos()  # Ko ko ko ko ko ko

or2 = Orzel("Orzel", 56)
or2.latam()
or2.wydaj_odglos()
# Tu Orzel Lecę z szybkością 56
# kier kir kier kier

# TypeError: Can't instantiate abstract class Sowa without an implementation
# for abstract method 'wydaj_odglos'
# sow = Sowa("Sowa", 20)

# polimorfizm
# obiekty róznych klas maja te same pola i metody
# można je traktowac jako obiekty wspolnej klasy Ptak
lista = [or2, kur2]
for i in lista:
    i.wydaj_odglos()
# kier kir kier kier
# Ko ko ko ko ko ko
or2.polowanie()
# Tu Orzel rozpoczynam polowanie
