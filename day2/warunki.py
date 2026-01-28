# warunki
# instrukcje warunkowe
# instrukcje sterowanie przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu
# wyrażenie w warunku musi zwrócic typ bool

odp = True
if odp:
    print("Test")

if odp: print("Test")

# odp = False
if odp:  # blok programu wykonany gdy warunek True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")

odp = "Radek"  # wpisanie danych do zmiennej
if odp:  # czy cokolwiek jest w zmiennej
    print("Dane zostały wczytane")
# Dane zostały wczytane

if odp == "Radek":  # porównanie
    print("Jesteś Radek")
# Jesteś Radek

odp = 0
if odp:
    print("Działa")
else:  # w innym przypadku, wartość domyślna
    print("Zero -> False")
# Zero -> False

a = "Radek"
# długosc wiecej niz 3
# wypisze tekst: Długośc wynosi: dl, więcej niż 3

if len(a) > 3:
    print(f"Długość wynosi: {len(a)}, wicej niż 3")

n = len(a)
if n > 3:
    print(f"Długość wynosi: {n}, wicej niż 3")

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długość wynosi: {n}, wicej niż 3")
#
# podatek = 0
#
# zarobki = int(input("Podaj zarobki:"))
#
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi: {zarobki * podatek} pln.")
# dodac podatek 20%, dla zarobków od 10000 do 39999
# Podaj zarobki:15000
# Podatek wynosi: 3000.0 pln.

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi: {rabat}")
# Rabat wynosi: 25

# operator warunkowy
rabat = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi: {rabat}")

# napisac tezt z...
# trzy pytania
# dodac punktację

# punkty = 0
# odp = input("podaj rok Chrztu Polski")
# if odp.strip().casefold() == '966':
#     print("Prawidłowa odpowiedź")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Doucz się")
#
# odp = input("Czy Ala ma kota?")
# if odp.strip().casefold() == 'tak'.strip().casefold():
#     print("Prawidłowa odpowiedź")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Doucz się")
#
# print("Zdobyłes pkt:", punkty)
# print(f"Zdobyłes pkt: {punkty}")
# podaj rok Chrztu Polski966
# Prawidłowa odpowiedź
# Czy Ala ma kota?tak
# Prawidłowa odpowiedź
# Zdobyłes pkt: 2
# Zdobyłes pkt: 2

# zasymulejemy system zbierania logów
# zmienna: przechowuje typ systemu, console, email, inny
# console: "Stało się coś strasznego"
# email: "System email"
# dodac do listy tłumaczenie błedu
# zmienna: przechowuje poziom błedu: error, medium i inny

lista_b = []
alert_system = "email"
error_level = "error"

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error_level == "error":
        lista_b.append("Krytyczny")
    elif error_level == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("inny")
else:
    print("Inny system")

print(lista_b)

# System email
# ['Krytyczny']
