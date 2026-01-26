tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\.venv\Scripts\python.exe C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\day1\teskty.py
# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
""" Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
# 13:50

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie

# Witaj Świecie
# 01234567890..
print(tekst[2])  # t, indeks numer 2, pozycja 3

print(tekst.index("Ś"))  # indeks numer 6

print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("w"))  # występuje 1 raz
print(tekst.lower().count("w"))  # występuje 2 razy

print(tekst.count("j", 0, 4))  # występuje 0 razy, z prawej zbiór otwarty

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie biłaych znaków, wiodących i kończących (spacji)
print(tekst.removesuffix("Świecie").strip()) # "Witaj"
