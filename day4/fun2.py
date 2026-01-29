# funkcje zwracające wynik
# kończy się: return (zwróć)

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj(4, 9))  # 13

print(odejmij(6, 9, 12))
wynik = odejmij(6, 8, 12)
print("Wynik:", wynik)

print(odejmij())  # 0
print(odejmij(a=9, b=7, c=90))  # -88
print(odejmij(1, 2, 3))  # -4
print(odejmij(1, 2))  # -1
print(odejmij(1, b=9, c=90))  # -98


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(kwota=1000, vat=8))

# 1230.0
# 1080.0
# 1080.0

zm = oblicz_vat(1000)
if zm == 1230:
    print("OK")  # OK

print(dodaj(5, 7) + odejmij(5, 89))
# -72
