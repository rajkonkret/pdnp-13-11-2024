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
