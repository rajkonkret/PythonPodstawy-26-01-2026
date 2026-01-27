# słownik - para klucz:wartosc
# {"user" : "Radek"}
# odpowiednik jsona
# klucze nie mogą się powtarzac

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodanie eleemntów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
# dodac klucz wiek
dictionary['wiek'] = 50
print(dictionary)  # {'imie': 'Radek', 'wiek': 50}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 50])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 50)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 50}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek

dictionary['imie'] = ["Radek", "Tomek", "Magda"]
print(dictionary)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}
print(dictionary['imie'])  # ['Radek', 'Tomek', 'Magda']
print(dictionary['imie'][1])  # Tomek

# print(dictionary["Imie"])  # KeyError: 'Imie'
print(dictionary['Imie'.lower()])  # ['Radek', 'Tomek', 'Magda']

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

name1 = "GROSS"
name2 = "groẞ"

print(name1.lower() == name2.lower())  # False
""" Return a version of the string suitable for caseless comparisons. """
print(name1.casefold() == name2.casefold())  # True

dictionary.update({"data": "12-12-2050"})
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50, 'data': '12-12-2050'}
# [('imie', 'Radek'), ('wiek', 50)] - lista krotek

dict_small = {'x': 2}
dict_small.update([("y", 3), ("z", 5)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 5}

# input() - pozwala wprowadzic dane do komputera np.:  z klawiatury
# zwraca stringa
# tekst = input("Podaj tekst")
# print(tekst)
# Podaj tekstRadek
# Radek

# napisac aplikacje kalulator
# a = int(input("Podaj pierwszą liczbę:"))
# b = input("Podaj drugą liczbę:")
# print(a + float(b))  # 3.0

# napisac aplikację słownik pol-ang
pol_ang = {'pies': "dog", "kot": "cat", "dach": "roof"}
print("Znam takie słówka:", pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia:")
print(f"Prawidłowa odpowiedż dla: {odp} to: {pol_ang.get(odp.strip().casefold(), "Nie ma")}")
# Znam takie słówka: dict_keys(['pies', 'kot', 'dach'])
# Podaj słówko do przetłumaczenia: Pies
# Prawidłowa odpowiedż dla:  Pies to: dog