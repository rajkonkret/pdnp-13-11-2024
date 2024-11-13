tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
tekst.upper()
print(tekst)  # Witaj Świecie
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE

print(tekst)  # Witaj Świecie

# zamiana na małe litery
tekst_lower = tekst.lower()
print(tekst_lower)  # witaj świecie
print(tekst)  # Witaj Świecie

# Witaj Świecie
# 0123456789... indeksy numerowane od 0
print(tekst[1])  # i

print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # 0 razy bo indeksy 0123
print(tekst.count("j", 0, 4))  # sam podstawia podpowiedzi
print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

tekst_zamiana = "Witaj dobry Świecie"
print(tekst_zamiana.replace("dobry", ""))  # "Witaj  Świecie"
print(tekst_zamiana.replace(" dobry", ""))  # "Witaj Świecie"

print(tekst.removesuffix("Świecie").strip())  # "Witaj" - strip() - usunięcie białych znaków z przodu i z tyłu (spacji)

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
# b - typ bajtowy
# \x - zpis liczby w systemie szesnastkowym
# \xc5 - 197 dziesiętnie
print(type(encode_s))  # <class 'bytes'>

print(encode_s.decode('utf-8'))  # "Witaj Świecie"

imie = "Radek"

# f - string - sformatowane teksty
tekst_format = f"Mam na imię {imie} i lubię pythona"
print(tekst_format)  # Mam na imię Radek i lubię pythona

tekst_format2 = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format2)
# "	Mam na imię Radek
# i lubię pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s"  # %s - podstaw łancuch znaków (str)
print(starszy % imie)  # Witaj Radek

print("Witaj {}".format(imie))  # Witaj Radek
print("Witaj {} {}".format(imie, "Kowalski"))  # Witaj Radek Kowalski

# tekst wielolinijkowy
print("""Tekst
    wielolinijkowy""")

# "Tekst
#     wielolinijkowy"

"""
Komentarz 
wielolinijkowy
"""

print(len(tekst_format2))  # 37, len() - sprawdzenie długości
