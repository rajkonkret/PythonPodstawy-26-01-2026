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
