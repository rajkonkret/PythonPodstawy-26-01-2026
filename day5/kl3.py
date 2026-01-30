class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Konstruktor - metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year

        # pole prywatne, hermetyzacja
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkośc wynosi: {self.__predkosc} km/h")

    def hamuj(self):
        if self.__predkosc > 0:
            self.__predkosc -= 10
        else:
            self.__predkosc = 0

        self.__zmiana_biegu()

    # name mangling
    def __zmiana_biegu(self):
        print('Zmiana biegu')


car = Car("VW Arteon", 2026)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car.__predkosc)  # 50
car.licznik()  # Prędkośc wynosi: 50 km/h
car.__predkosc = 0
car.licznik()
# Prędkośc wynosi: 50 km/h
# Prędkośc wynosi: 50 km/h
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkośc wynosi: 0 km/h

# enkapsulacja - zahermetyzowanie pol i wystawienie metod do zapisu i odczytu
# settery, gettery
