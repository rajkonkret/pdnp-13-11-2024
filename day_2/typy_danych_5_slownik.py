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
# print(dictionary['Imie']) # KeyError: 'Imie'
print(dictionary['Imie'.lower()])  # Tomek
print(dictionary.get('Imie'))  # gdy nie ma klucza zwróci None
print(dictionary.get('Imie', 'Zenek'))  # gdy nie ma klucza zwróci Zenek bo tak ustawiliśmy wartość domyślną

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 4)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 4}

# input() - pobiera dane od użytkownika
# tekst = input("Podaj imię")
# print("Masz na imię", tekst)
# Podaj imięRadek
# Masz na imię Radek

# napisac apliakcje kalkulator
# podaj dwie liczby -> input x 2
# wyswietl wynik (dodawania) -> print
# # input zwraca str
# a = int(input("Podaj pierwszą liczbę"))  # mozna rzutowac na liczbę podczas pobierania
# b = input("Podaj drugą liczbę")
# print("Wynik:", a + float(b)) # można juz przy obliczaniu

# Podaj pierwszą liczbę5
# Podaj drugą liczbę6
# Wynik: 11.0

# napisac aplikację słownik
# pol - ang
# słownik z naszymi hasłami i tłumaczeniami
# wyswietlic hasła jakie znamy (klucz)
# pobrac od użytkownika co chce przetłumaczyć
# wypisać tłumaczenie

pol_ang = {'kot': 'cat', 'pies': 'dog', "dach": "roof"}
print("Znam takie słówka", pol_ang.keys())
odp = input("Podaj słowko do przetłumaczenia")
# print(pol_ang[odp.strip().lower()])
print(pol_ang.get(odp.lower().strip(), "nie mo"))
print(pol_ang.get(odp.casefold().strip(), "nie mo"))
""" Return a version of the string suitable for caseless comparisons. """
# nie tylko omija problem małe duże litery ale też np niemieckie znaki typu ss -> ß
