# pętla  - możliwość wykonania kodu wielokrotnie
# for - pętla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)

for i in range(20):
    pass  # nic nie rób

for _ in range(15):  # niema zmienna
    print("Test podłoga")
    print(_)  # można odczytać wartość

for i in range(5):
    print(i + 2)
    print(i * 2)

# przerobić lotto na pętle
# zapisac wynik do listy

lista_kule = list(range(1, 50))  # od 1 do 49
lista_wynik = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    print(wyn)
    lista_kule.remove(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)
# [28, 36, 40, 42, 14, 5]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")

lista3 = []
for i in range(10):
    if i % 2 == 0:
        lista3.append(i)

print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:  # podstawi kolejne elementy z listy
    print(c)

lista_nazwy = ["Ala", "Tomek", "Zenek", "Basia"]
for p in lista_nazwy:
    print(p)
# Ala
# Tomek
# Zenek
# Basia

for c in lista3:
    if c > 4:
        print(c, "większe do 4")
    elif c == 4:
        print(c, "równe 4")
    else:
        print(c, "mniejsze od 4")

    print(c)
print("Po zakońćzeniu pętli")
# 0 mniejsze od 4
# 0
# 2 mniejsze od 4
# 2
# 4 równe 4
# 4
# 6 większe do 4
# 6
# 8 większe do 4
# 8
# Po zakońćzeniu pętli

for i in range(10, 0, -2):  # (start, stop, krok) ujemny krok, licznik w dół
    print(i)

for i in range(-10, 0):
    print(i)

imiona = ["Radek", "Tomek", 'Agata', "Marek"]

for o in imiona:
    print(o)
# Radek
# Tomek
# Agata
# Marek

# 0 Radek
for i in range(len(imiona)):
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

# enumerate() - zwraca numer i eleemnt kolekcji
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Agata')
# (3, 'Marek')
a, b = (3, 'Marek')
for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Agata
# 4 Marek

imiona = ["Radek", "Tomek", 'Agata', "Marek", "Magda"]
wiek = [44, 56, 23, 38]

# # Radek 44
# for p in imiona:
#     print(p, wiek[imiona.index(p)])
# # Radek 44
# # Tomek 56
# # Agata 23
# # Marek 38
# IndexError: list index out of range przy rózżnych dlugościach list

# zip() - łączy kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 56)
# ('Agata', 23)
# ('Marek', 38)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 56
# Agata 23
# Marek 38

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 56))
# (2, ('Agata', 23))
# (3, ('Marek', 38))
a, b = (3, ('Marek', 38))
print(a, b)  # 3 ('Marek', 38)
c, d = ('Marek', 38)
print(c, d)
(a, (c, d)) = (3, ('Marek', 38))
print(a, c, d)  # 3 Marek 38

for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 56
# 2 Agata 23
# 3 Marek 38