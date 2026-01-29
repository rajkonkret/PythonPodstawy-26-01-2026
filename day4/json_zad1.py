# {"firstName":"John", "lastName":"Doe"}
#   {
#         "description": "\u201eName mangling\u201d to mechanizm zmiany nazwy atrybut\u00f3w klasy, kt\u00f3re s\u0105 zdefiniowane jako prywatne, co ma na celu unikni\u0119cie konflikt\u00f3w nazw w klasach pochodnych.",
#         "example": "print(\"Przyk\u0142ad do: Co to jest \u201ename mangling\u201d w Pythonie?\")",
#         "id": 30,
#         "level": "podstawowy",
#         "term": "Co to jest \u201ename mangling\u201d w Pythonie?"
#     },

# json - dane typu klucz wartość
# typ danych do wymiany danych pomiędzy klient-serwer
# odpowiednikiem jsona w pythonie jest słownik

import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

# zapis jako json
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)

# beautify
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# sortowanie kluczy wg kolejności alfabetycznej
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

# wczytanie danych do słownika
with open('nasze_dane.json', "r") as file:
    data = json.load(file)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>

print(data['name'])  # Radek

# zamiana słownika na jsona (tekst)
json_tekst = json.dumps(data)
print(json_tekst)  # {"age": 40, "czy_pali": null, "name": "Radek"}
print(type(json_tekst))  # <class 'str'>

# zamiana jsona na  słownik
dict_json = json.loads(json_tekst)
print(dict_json)
print(type(dict_json))
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>

resp = r'''{
         "description": "\u201eName mangling\u201d to mechanizm zmiany nazwy atrybut\u00f3w klasy, kt\u00f3re s\u0105 zdefiniowane jako prywatne, co ma na celu unikni\u0119cie konflikt\u00f3w nazw w klasach pochodnych.",
         "example": "print(\"Przyk\u0142ad do: Co to jest \u201ename mangling\u201d w Pythonie?\")",
         "id": 30,
         "level": "podstawowy",
         "term": "Co to jest \u201ename mangling\u201d w Pythonie?"
     }'''

dane = json.loads(resp)

# wypisac klucze z tego slownika
print(dane.keys())
# dict_keys(['description', 'example', 'id', 'level', 'term'])

for i in dane:
    print(i)

# description
# example
# id
# level
# term