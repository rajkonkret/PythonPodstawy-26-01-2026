import random

# działania na liczbach losowych

#  """Return random integer in range [a, b], including both end points.
#        """
print(random.randint(1, 100))  # int od 1 do 100 włacznie

print(random.randrange(1, 100))  # od 1 do 99
print(random.randrange(5))  # int od 0 do 4

print(random.random())  # float, 0.08086122087233028, od 0 do 0.999999999
print(random.random() * 7)  # float, 4.062106231875812, od 0 do 6.999999999
print(round(random.random() * 6))  # 4

lista = [67, 45, 32, 68, 90, 42, 69]
print(lista[random.randrange(len(lista))])  # element: 42

print(random.choice(lista))  # 67

# stworzyc listę kul
# wylosować kulę z listy
# wyświetlic kulę
# usunąc kulę
# ctrl shift f - wyszukiwanie w całym projekcie

lista_kule = list(range(1, 50))  # od 1 do 49
wyn = random.choice(lista_kule)
print(wyn)
lista_kule.remove(wyn)

print(random.choices(lista_kule, k=6))  # [32, 49, 23, 41, 32, 25], z powtórzeniami
print(random.sample(lista_kule, k=6))  # [38, 33, 47, 4, 9, 32] bez powtórzeń
print(random.sample(lista_kule, 6))  # [38, 33, 47, 4, 9, 32] bez powtórzeń
# [2, 23, 24, 33, 41, 48]
# [36, 47, 26, 17, 38, 31]
