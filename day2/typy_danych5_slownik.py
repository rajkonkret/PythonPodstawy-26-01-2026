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
print(dictionary) # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}
