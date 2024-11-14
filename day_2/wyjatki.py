# wyjątki - błęy podczas wykonywania programu
# program rzuca wyjątek

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-13-11-2024\day_2\wyjatki.py", line 4, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1

# obsługa wyjątków
try:
    # print(5 / 0)
    # print(int("A"))
    # print(3 / "0")
    wynik = 90 / z
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Bład wartości")
except TypeError:
    print("Błąd typu")
except Exception as e:  # zapisanie błedu do zmiennej o nazwie "e"
    print("Bład", e)
else:  # wykona się tylkko kiedy nie ma błedu
    print("Wynik", wynik)
finally:  # wykona się zawsze i gdy będzie błąd i gdy nie będzie błędu
    print("---------------")

print("Program nadal działa")
# Nie dziel przez zero
# Program nadal działa
# Bład wartości
# Program nadal działa
# Błąd typu
# Program nadal działa
# Bład name 'z' is not defined
# Program nadal działa
# Wynik 30.0
# Program nadal działa

# finnally
# Bład name 'z' is not defined
# ---------------
# Program nadal działa
# Wynik 30.0
# ---------------
# Program nadal działa

# try except [else finally]
