import sys

wiek = 47
rok = 2024
temp = 36.6  # float

print(temp)
print(type(temp))  # <class 'float'>
temp2 = 36, 6
print(temp2)  # (36, 6)

print(wiek + rok)  # 2071
print(wiek - rok)  # -1977
print(wiek * rok)  # 95128
print(wiek / rok)  # 0.023221343873517788

print(rok // wiek)  # 43, część całkowita z dzielenia
print(rok % wiek)  # reszta z dzielenia, 3
print(10 % 3)  # reszty 1, modulo

print(wiek ** rok)
print(len(str(wiek ** rok)))  # długośc 3385
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# float ma bład zaokrąglenia
# aby ominąc mamy typ decimal
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
print(sys.float_info)
# sys.float_info(
#     max=1.7976931348623157e+308,
#     max_exp=1024,
#     max_10_exp=308,
#     min=2.2250738585072014e-308,
#     min_exp=-1021,
#     min_10_exp=-307,
#     dig=15,
#     mant_dig=53,
#     epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzanie zmiennej {temp} {wiek}")  # Sprawdzanie zmiennej 36.6 47
print(f"""
{wiek}
    {temp}""")
# "47
#     36.6"

# typ logiczny
# prawda lub fałsz
# 1 - prawda, 0 - fałsz
# True, False - obowiązkowo z dużej litery
czy_znasz_python = True
print(czy_znasz_python)
print(type(czy_znasz_python))  # typ logiczny, <class 'bool'>, boolean

print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # bool() rzutowanie na typ logiczny, True
print(bool(100))  # True
print(bool(-100))  # True
print(bool("radek"))  # True

print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False; None - nic, stan nieokreślony, odpowiednik null

# and, or , not
print(True and False)  # False
print(True or False)  # True

print(not True)  # False

a = 8
b = 6

# wynik porównan jest bool
print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 8 > 6 = True
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 8 < 6 = False

print(f"Porównanie {a <= b= }")
print(f"Porównanie {a >= b= }")
# Porównanie a <= b= False
# Porównanie a >= b= True

print(f"Porównanie {a} == {b} = {a == b}")  # czy a równa się b, Porównanie 8 == 6 = False
print(f"Porównanie {a} != {b} = {a != b}")  # czy różne?, Porównanie 8 != 6 = True
