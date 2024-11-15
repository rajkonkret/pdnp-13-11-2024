# funkcje zwracające wynik
# kończą się słówkiem return


def dodaj(a, b):
    return a + b


def odejmij(a, b=0, c=0):
    return a - b - c


print(dodaj(6, 89))  # 95
wynik = dodaj(34, 78)
print("Wynik", wynik)  # Wynik 112

print(odejmij(10))
print(odejmij(10, 34))
print(odejmij(10, 34, 56))
print(odejmij(10, c=34, b=56))
# 10
# -24
# -80
# -80

print(dodaj(34, 67) + dodaj(67, 90))  # 258
