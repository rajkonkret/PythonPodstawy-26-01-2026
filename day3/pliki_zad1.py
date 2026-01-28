# działania z plikami
# context manager
# with - context manager w pythonie

# filehandler
# \n - nowa linia

# w - tworzy nowy plik
# jesli juz istnieje zostanie usunięty
with open("test.log", "w", encoding='utf-8') as f:
    f.write("Powitanie\n")

# x - tworzy nowy plik
# jesli plik istnieje, przrywa działanie
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x", encoding='utf-8') as f:
#     f.write("Powitanie\n")

with open("test.log", "w", encoding='utf-8') as f:
    f.write("Parametr 1\n")
    f.write("Parametr 2\n")
    f.write("Parametr 3\n")
    f.write("Parametr 4\n")

with open("test.log", "a", encoding='utf-8') as file:
    file.write("Dodane1\n")
    file.write("Dodane2\n")
    file.write("Dodane3\n")
    file.write("Dośdane3\n")

with open("test.log", "r", encoding='utf-8') as file:
    lines = file.read()

print(lines)
# Parametr 2
# Parametr 3
# Parametr 4
# Dodane1
# Dodane2
# Dodane3
# Dośdane3