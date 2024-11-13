import sys

print()  # wypisz/wydrukuj
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
# ctrl d - powielenie
print('Nazywam się Radek')  # Nazywam się Radek

# ctrl / - komentarz
# print('Nazywam się Radek")
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-13-11-2024\day_1\pierwszy.py", line 13
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 13)
#
# Process finished with exit code 1 - code 1 oznaczza bład

# type() - sprwdzenie typu danych
print(type("Radek"))  # <class 'str'> string, tekst
print("39")  # 39
print(type("39"))  # <class 'str'>

print(39)  # 39
print(type(39))  # <class 'int'>, integer, liczby całkowite

print(sys.int_info)
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,
#     str_digits_check_threshold=640)

print("39" + "39")  # konkatenacja tekstów 3939, łączenie
print(39 + 39)  # 78
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str
# silne typowanie - nie zamienia sam typów
# musimy jawnie zamienic
print(int("39") + 39)  # int() - rzutowanie (zamiana) na int, 78
print("39" + str(39))  # str() - zamiana na string, tekst 3939

print(5 * "8")  # 88888
print(5 * 8)  # 40
print(5 * int("8"))  # 40
print(int("0"))  # 0

# zmienna - pudełko na dane
# typowanie dynamiczne
liczba = 39
print(type(liczba))  # <class 'int'>
print(liczba)
print("5" * liczba)  # 555555555555555555555555555555555555555

liczba = "39"
print(type(liczba))  # <class 'str'>

# tylko podpowiedź, nie jest to deklaracja typu!!!
liczba: int = 100

name = 90
print(type(name))
# print(name + "Kowalski")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
name: str = "Radek"  # :str - to jest tylko podpowiedź
print(name)  # Radek

age = 56
print(age)
print(type(age))
# 56
# <class 'int'>

# nazwy zmiennych małą literą
# zmienna powinna podpowiadać co przechowuje
# snake_case
# wiek_usera
