# krotka (tupla) - kolekcja niemutowalna
# pozwalaefektywniejj zarządzać pamięcią
# krotka jednoelementowa - stała - zmienna

tupla = "Radek"
print(type(tupla))  # <class 'str'>

tupla_2 = ("Radek")
print(type(tupla_2))  # <class 'str'>

tupla_3 = "Radek",
print(type(tupla_3))  # <class 'tuple'>

# nawias ()  jest opcjonalny
# krotka musi mieć minimum jeden przecinek

# PEP8 zaleca przy krotce jednoelementowej dodawac ()
tupla_4 = ("Radek",)
print(type(tupla_4))  # <class 'tuple'>
print(tupla_4)  # ('Radek',)

temp = 36, 6
print(type(temp))  # <class 'tuple'>

# można z () lub bez
# tupla_liczby = 43, 5, 22.34, 11, 200
tupla_liczby = (43, 5, 22.34, 11, 200)
print(type(tupla_liczby))
print(tupla_liczby)  # (43, 5, 22.34, 11, 200)

# tupla_liczby[2] = 123  # TypeError: 'tuple' object does not support item assignment
del tupla_liczby  # można usunąć cała tuplę
# print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined

tupla_imiona = "Radek", 'Tomek', "Marek", 'Anna', "Monika", "Zenek", "Tadeusz"
print(tupla_imiona)  # ('Radek', 'Tomek', 'Marek', 'Anna', 'Monika', 'Zenek', 'Tadeusz')
print(type(tupla_imiona))  # <class 'tuple'>
print(len(tupla_imiona))  # 7

print(tupla_imiona.index("Monika"))  # indeks numer 4
print(tupla_imiona.count("Radek"))  # występuje 1 raz
