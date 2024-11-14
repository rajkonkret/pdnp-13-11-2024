# słownik - para klucz-wartosc
# {'user': 'Radek', "wiek': 70}
# słownik jest odwzorowaniem jsona w pythonie
# {"firstName":"John", "lastName":"Doe"}

# pusty słownik
dictionary = dict()
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

dictionary_1 = {}
print(type(dictionary_1))  # <class 'dict'>
print(dictionary_1)  # {}

# dodawanie elemntów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 38
print(dictionary)  # {'imie': 'Radek', 'wiek': 38}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 38])
# dict_items([('imie', 'Radek'), ('wiek', 38)])

# nadpisanie elemntów
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38}

# wypisanie wartości dla danego klucza
print(dictionary['imie'])  # Tomek
