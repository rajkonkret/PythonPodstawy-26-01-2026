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
