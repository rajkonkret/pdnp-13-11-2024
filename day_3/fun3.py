# zmienne globalne
a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # uzywa zmiennych globalnych


def dodaj3():
    global a
    a = 9  # globalne a zostanie nadpisane
    b = 78
    print(a + b)


def dodaj4(b):
    global a
    a = b
    print(a + b)


print(a + b)
print(f"Wartość a z góry (globalna) {a=}")  # Wartość a z góry (globalna) a=10
dodaj()  # 15
print(f"Wartość a z góry (globalna) {a=}")  # Wartość a z góry (globalna) a=10
dodaj2()  # 20
print(f"Wartość a z góry (globalna) {a=}")  # Wartość a z góry (globalna) a=10
dodaj3()  # 87
print(f"Wartość a z góry (globalna) {a=}")  # Wartość a z góry (globalna) a=9
print(a + b)
