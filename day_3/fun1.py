# funkcja - kod który wykonujemy wielokrotnie w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# w miejscu deklaracji nie uruchamie się
# zeby wykonać funkcję musimy ją wywołać

a = 6
b = 8


# deklaracja funkcji
# PEP8 zaleca by funkcje były małymi literami
# PEP8 zaleca odstep dwóch lini od deklaraacji funkcji i programu
def dodaj():
    print(a + b)


# obowiązkowo musimy przekazac argumenty a i b
def dodaj2(a, b):
    print(a + b)


def odejmij(a, b, c=0):  # c ma wartość domyślną
    print(a - b - c)


# wywołąnie funkcji
# nazwa_funkcji i nawiasy ()
dodaj()  # 14
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# argumenty przekazane po pozycji
dodaj2(10, 35)  # 45
odejmij(1, 2, 3)  # -4
odejmij(1, 2)  # c=0 wynik -1

# argumenty przekazane po nazwie
odejmij(1, c=9, b=7)
odejmij(c=9, a=10, b=78)

# odejmij(c=9,3,4) # SyntaxError: positional argument follows keyword argument
odejmij(1, 2, c=9)

# te funkcje nie zwracją wyniku
print(dodaj())  # None

# print(dodaj() + dodaj())  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
