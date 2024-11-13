user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001
print(type(wersja))  # <class 'float'>, liczby zmiennoprzecinkowe

liczba = 789123456678  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.
# %s - str
# %d - digit
# tu są sprawdzane typy
# print("Witaj %d, masz teraz %s lat." % (user, wiek))  # TypeError: %d format: a real number is required, not str

print("Witaj %(user)s, masz teraz %(wiek)d lat. %(user)s" % {'user': user, "wiek": wiek})
# Witaj Tomek, masz teraz 39 lat. Tomek

print("Witaj {}, masz teraz {} lat".format(user, wiek))  # Witaj Tomek, masz teraz 39 lat

print(f"Witaj {user}, masz teraz {wiek} lat.{{")  # Witaj Tomek, masz teraz 39 lat.{
print("Witaj", user)  # Witaj Tomek

print("Uzywamy wersji Pythona %i" % 3)  # Uzywamy wersji Pythona 3
print("Uzywamy wersji Pythona %f" % 3)  # Uzywamy wersji Pythona 3.000000
print("Uzywamy wersji Pythona %.2f" % 3)  # Uzywamy wersji Pythona 3.00
print("Uzywamy wersji Pythona %.1f" % 3)  # Uzywamy wersji Pythona 3.0
print("Uzywamy wersji Pythona %.0f" % 3)  # Uzywamy wersji Pythona 3
print("Uzywamy wersji Pythona %.f" % 3.9)  # Uzywamy wersji Pythona 4 - zaokrągla przy wyświetlania

print(f"Uzywamy wersji python {wersja}")
print(f"Uzywamy wersji python {wersja:.1f}")
print(f"Uzywamy wersji python {wersja:.2f}")
print(f"Uzywamy wersji python {wersja:.0f}")
# Uzywamy wersji python 3.90001
# Uzywamy wersji python 3.9
# Uzywamy wersji python 3.90
# Uzywamy wersji python 4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:<15}")  # "Tomek          "
print(f"{user:^25}")  # "          Tomek          "

print(liczba)  # 789123456678
print(f"Nasza duża lizba {liczba:,}")  # Nasza duża lizba 789,123,456,678
print(f"Nasza duża lizba {liczba:_}")  # Nasza duża lizba 789_123_456_678
print(f"Nasza duża lizba {liczba:_}".replace("_", "."))  # Nasza duża lizba 789_123_456_678
print(f"Nasza duża lizba {liczba:_}".replace("_", " "))  # Nasza duża lizba 789_123_456_678
# Nasza duża lizba 789.123.456.678
# Nasza duża lizba 789 123 456 678

liczba2 = 15000000000000  # int
liczba3 = 15_000_000_000_000
print(type(liczba3))  # <class 'int'>
print(liczba3)  # 15000000000000
