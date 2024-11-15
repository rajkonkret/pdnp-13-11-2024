# klasa - element programowannia obiektowego
# klasa - szablon, przepis
# wskazuje cechy i funcje
# cechy = zmienne
# fumkcje, metody
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
# definicja klasy nie urchamia klasy
# tworzenie obiektu uruchamia metode inicjalizującą (konastruktor)

# definicja klasy
# PEP8 - nazwy kals z duzej litery
# komentarz wielolinijkowy to jest dokumwntacja
class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"


print(Human.__doc__)

# Klasa Human opisująca człowieka w pythonie
print(print.__doc__)

# cd .\day_3\ przejscie do katalogu day_3
# pydoc -b - serwer z dokumentacją
# pydoc -w kl1 - wygenerowanie pliku html z dokumentacją
cz1 = Human()
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz1.wiek = 89
cz1.imie = "Kasia"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Kasia
# 89
# k
