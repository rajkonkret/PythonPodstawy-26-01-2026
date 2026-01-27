# kolekcje

# lista - przechowuje dowolną ilość danych, róznego typu na raz
# zachowuje kolejnośc podczas dodawania

# pusta lista
lista = []
print(type(lista))  # <class 'list'>
print(lista)  # []

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# dodawanie do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Piotr")
lista.append("Zenek")
lista.append("Anna")
lista.append("Magda")

print(lista)  # ['Radek', 'Tomek', 'Piotr', 'Zenek', 'Anna', 'Magda']

print(len(lista))  # 6 elementów
# ['Radek', 'Tomek', 'Piotr', 'Zenek', 'Anna', 'Magda']
#      0       1         2        3       4        5

print(lista[2])  # Piotr
print(lista[4])  # Anna

# print(lista[10])  # IndexError: list index out of range

print(lista[5])  # Magda
print(lista[len(lista) - 1])  # Magda
print(lista[-1])  # ostatni element, Magda
print(lista[-2])  # Anna
# ['Radek', 'Tomek', 'Piotr', 'Zenek', 'Anna', 'Magda']
#      0       1         2        3       4        5
#      -6       -5       -4       -3       -2      -1

# slicowanie - fragment listy
print(lista[0:3])  # [start:stop], ['Radek', 'Tomek', 'Piotr'] indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Piotr']

print(lista[2:])  # ['Piotr', 'Zenek', 'Anna', 'Magda'], z ostatnim włącznie
print(lista[2:5])  # ['Piotr', 'Zenek', 'Anna'], bez ostatniego
print(lista[2:9])  # ['Piotr', 'Zenek', 'Anna', 'Magda']
print(lista[12:26])  # []

print(lista[:])
# ['Radek', 'Tomek', 'Piotr', 'Zenek', 'Anna', 'Magda']

# ['Radek', 'Tomek', 'Piotr', 'Zenek', 'Anna', 'Magda']
#      0       1         2        3       4        5
#      -6       -5       -4       -3       -2      -1
print(lista[-2:0])  # [4:0], []
print(lista[0:-2])  # [0:4], ['Radek', 'Tomek', 'Piotr', 'Zenek']

# range() - generuje liczby z zakresu (int)
lista_15 = list(range(15))
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista[::2])  # ['Radek', 'Piotr', 'Anna'], [start:stop:krok]
print(lista_15[::3])  # [0, 3, 6, 9, 12]

print(list(range(0, 15, 2)))  # (start, stop, krok)
# [0, 2, 4, 6, 8, 10, 12, 14]

# wyswietlic listę w odwrotnej kolejnosci
print(lista[::-1])
# ['Magda', 'Anna', 'Zenek', 'Piotr', 'Tomek', 'Radek']

# numpy - biblioteka do pracy z tablicami/macierzami
# nadpisanie elementu na wskazanym indeksie
lista[3] = "Asia"
print(lista)  # ['Radek', 'Tomek', 'Piotr', 'Asia', 'Anna', 'Magda']

# wstawienie elemntu na wskazanym indeksie, pomiędzy inne elementy
lista.insert(1, "Ola")
print(lista)  # ['Radek', 'Ola', 'Tomek', 'Piotr', 'Asia', 'Anna', 'Magda']

# stworzyc pusta liste, dodac element na indeksie 1
lista_darek = []
lista_darek.insert(1, "Darek")
print(lista_darek)  # ['Darek']

# usuniecie elementu z listy po elemencie,, pierwszy napotkany
lista.remove("Tomek")
print(lista)  # ['Radek', 'Ola', 'Piotr', 'Asia', 'Anna', 'Magda']
# dodajemy np.: Piotr, usunąc Piotr
lista.append("Piotr")
print(lista)
lista.remove("Piotr")
print(lista)  # ['Radek', 'Ola', 'Asia', 'Anna', 'Magda', 'Piotr']

# usunięcie po indeksie, zwraca element usunięty
# pop()
print(lista.pop(2))  # Asia
zmienna = lista.pop(-1)
print(zmienna)  # Piotr

print(lista.pop())  # Magda, usunie ostatni element
print(lista)  # ['Radek', 'Ola', 'Anna']

# sprawdzenie indexu dla danego elementu, pierwszy napotkany
print(lista.index("Ola"))  # indeks 1

a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3
b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista2 = lista  # kopia adresu, referencji
lista_copy = lista.copy()  # kopia elementów listy do nowej listy
print(lista)
print(lista2)
# ['Radek', 'Ola', 'Anna']
# ['Radek', 'Ola', 'Anna']

lista.clear()  # usunięcie wszystkich elementów z listy
print(lista)
print(lista2)
print(lista_copy)  # ['Radek', 'Ola', 'Anna']

# id() - pokazuje referencje
print(id(lista))  # 1864296615872
print(id(lista2))  # 1864296615872
print(id(lista_copy))  # 1864298486016

liczby = [54, 999, 34, 12.34, 567, 999]
print(liczby)  # [54, 999, 34, 12.34, 567, 999]
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)  # [12.34, 34, 54, 567, 999, 999]

liczby = [54, 999, 34, 12.34, 567, 999, "A"]
# liczby.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

print(lista_copy)  # ['Radek', 'Ola', 'Anna']
lista_copy.sort()
print(lista_copy)  # ['Anna', 'Ola', 'Radek']

lista_copy.sort(reverse=True)  # sortowanie i odwróćenie
print(lista_copy)  # ['Radek', 'Ola', 'Anna']

lista_copy.reverse()  # tylko odwracanie
print(lista_copy)  # ['Anna', 'Ola', 'Radek']

liczby[3] = 666
print(liczby[0:3])
print(liczby[-3])
print(liczby)
# [54, 999, 34]
# 567
# [54, 999, 34, 666, 567, 999, 'A']

