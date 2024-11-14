dictionary = {'imie': 'Radek', 'nazwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>

# wypisze klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wypisanie wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
#  sep
#         string inserted between values, default a space.
for k, v in dictionary.items():
    print(k, v, sep="=>")
    # imie=>Radek
    # nazwisko=>Kowalski

# end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>", end="@@@@@@")
# imie=>Radek@@@@@@nazwisko=>Kowalski@@@@@@
print()
for k, v in dictionary.items():
    print(k, v, sep="=>", end="")
# imie=>Radeknazwisko=>Kowalski
print()
print("Nowa linia")
# imie => Radek
# nazwisko => Kowalski
# imie=>Radek
# nazwisko=>Kowalski
# imie=>Radek@@@@@@nazwisko=>Kowalski@@@@@@
# imie=>Radeknazwisko=>Kowalski
# Nowa linia

pol_ang = {'kot': 'cat', 'pies': 'dog', "dach": "roof"}
ang_pol = {}  # zamienic klucze z wartoścciami
for k, v in pol_ang.items():
    ang_pol[v] = k

print(ang_pol)  # {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

# { "klucz" : "wartosc" }
print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}
