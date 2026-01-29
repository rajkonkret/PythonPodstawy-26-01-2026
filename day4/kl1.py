# klasa - przepis, szablon
# cechy (zmienne)
# metody - funkcj w klasie
# obiekt - instancja klasy
# klasa musi zostac najpierw zadeklarowana
# tworzenie obiektu uruchamia funkcje inicjalizującą (konsrtruktor) __init__
# paradygmanty -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase, UpperCamelCase
class Human:
    """
    Klasa Human opisująca czlowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    # self - obiekt
    def powitanie(self):
        print(f"Nazywam się: {self.imie}")
        # print(f"Nazywam się: {cz1.imie}")

    def ruszaj(self):

        if self.plec == "m":
            print("Ruszył-em w drogę")
        else:
            print("Ruszył-am w drogę")


print(Human.__doc__)  # dokumentacja
# Klasa Human opisująca czlowieka w pythonie
# print(print.__doc__)
# pydoc - dokumentacja
# cd .\day4\ - wejscie do katalogu day4
# pydoc -b
# pydoc -w kl1

# tworzenie obiektów
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x0000019E188857F0>

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
#
# None
# k

cz1.imie = "Radek"
cz1.wiek = 50
cz1.plec = "m"

print(cz1.imie)  # Radek
print(cz1.wiek)  # 50
print(cz1.plec)  # m

cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 45

print(cz2.imie)  # Anna
print(cz2.wiek)  # 45
print(cz2.plec)  # k

cz2.powitanie()
cz1.powitanie()
# Nazywam się: Anna
# Nazywam się: Radek

cz1.ruszaj()
cz2.ruszaj()
# Ruszył-em w drogę
# Ruszył-am w drogę
