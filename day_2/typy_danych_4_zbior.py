# zbiór (set) - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # rzutowanie, zamian ana zbiór
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} - straciliśmy kolejność
print(type(zbior))  # <class 'set'>

# utworzenie pustego zbioru
zb2 = set()
print(zb2)  # set() - pusty zbiór
print(type(zb2))  # <class 'set'>

# dodanie leemntu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(24)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() - usunięcie pierwszego elementu
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}

zbior_copy = zbior.copy()
print(id(zbior_copy))
print(id(zbior))
# {66, 777, 11, 44, 18, 22, 24}
# 2452820267232
# 2452819957280
# ctrl / - komentarz

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}

# suma zbiorów - zwraca nowy zbiór
print(zbior | zbior_2)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}

# część wspólna - zwraca nowy zbiór
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# róznica
print(zbior - zbior_2)  # {24, 777, 66, 22}
print(zbior.difference(zbior_2))  # {24, 777, 66, 22}
print(zbior_2.intersection(zbior))  # {18, 11, 44}

# łączy zbiory w jeden, nadpisuje bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62)
print(type(krotka))  # <class 'tuple'>

lista = list(zbior)
print(lista)  # [66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62]
print(type(lista))  # <class 'list'>

# sprawdzenie czy element istnieje w kolekcji
print(999 in zbior_2)  # True
