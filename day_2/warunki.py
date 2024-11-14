# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# warunek musi zwrócic typ bool
# if

odp = True
print(bool(odp))  # True
# odp = False
# if odp: print()
if odp:
    # wciecie 4 spacje
    # blok wykonany gdy warunke True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Główna część programu")
# Connected to pydev debugger (build 242.23726.102)
# True
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Główna część programu
# debugger - narzędzie do analizy działania programu krok po kroku z możliwością sprawdzania stanu systemu, zmiennych itd

odp = "Radek"
print(bool(odp))
if odp:  # czy odp nie jest puste
    print("Radek")

if odp == "Radek":  # == - porównanie, sprawdzamy czy odp (równa) Radek
    print("To jest nadal Radek")

if odp == "Tomek":
    print("To jest Tomek")
else:  # w przeciwnym przypadku
    print("To nie jest Tomek")
# To jest nadal Radek
# To nie jest Tomek
# Indent Rainbow Plugin - pokazuje wyraźniej wcięcia i błedy wcięć

podatek = 0
zarobki = int(input("Podaj zarobki"))
# pierwszy True oznacza wyjscie z calego drzewa
if zarobki < 10_000:
    podatek = 0
elif zarobki < 30000:
    podatek = 0.2
elif zarobki < 100_000:
    podatek = 0.4
else:
    podatek = 0.9

print(f"podatek wynosi {podatek * zarobki}")
# od 10_000 do 29_999 podatek 0.2
