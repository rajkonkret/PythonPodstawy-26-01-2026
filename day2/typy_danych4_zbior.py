# zbior (set) - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# nie posiada indeksu
from day2.typy_danych2_lista import zmienna

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbiór
zb2 = set()  # tylko i wyłącznie słówkiem set()
print(zb2)  # set()

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(24)
zbior.add(24)
zbior.add(25)

print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24, 25}

# usuniecie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24, 25}

# pop()
print(zbior.pop())  # 33, usunie pierwszy element

zmienna = zbior.pop()
print(f"Zmienna: {zmienna}")
print('Zmienna:', zmienna)
# Zmienna: 66
# Zmienna: 66

zbior_copy = zbior.copy()
print(zbior_copy)  # {18, 22, 24, 777, 11, 44, 25}
print(id(zbior))
print(id(zbior_copy))
# 2249731503296
# 2249732942400

zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}

# suma zbiorów - zwraca nowy zbiór
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}

# część wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# róznica zbiorów
print(zbior - zbior_2)  # {24, 777, 22, 25}
print(zbior.difference(zbior_2))  # {24, 777, 22, 25}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# łączy zbiory, zmienia bazowy!!!
zbior.update(zbior_2)
print(zbior)
# {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}

