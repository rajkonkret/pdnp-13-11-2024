# pętle - pozwalaja wykonac dany fragment programu wielokrotnie
# for - iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(10):
    pass

for _ in range(5):  # niema zmienna
    print("Test podloga")
    # print(_)

# Test podloga
# Test podloga
# Test podloga
# Test podloga
# Test podloga

for i in range(10):
    print(i * 2)

# zrobic losowanie lotto za pomocą pętli
lista_kule = list(range(1, 50))
lista_wyn = []
for _ in range(6):  # 012345
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wyn.append(wyn)

print(lista_wyn)  # [46, 2, 26, 5, 29, 20]

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista_wyn:
    if c > 10:
        print("Większe od 10")
    else:
        print("Mniejsze od 10")
# Mniejsze od 10
# Większe od 10
# Mniejsze od 10
# Większe od 10
# Większe od 10
# Większe od 10

for i in range(0, 10, 2):  # start, stop, krok
    print(i)
# 0
# 2
# 4
# 6
# 8

for i in range(10, 0, -2):  # liczy w dół od 10 do 1 co drugi
    print(i)
# 10
# 8
# 6
# 4
# 2

for i in range(-10, 0):  # od -10 do -1
    print(i)

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print("Tylko dla c=2", c)
    print("Przy każdym elemenecie pętli")
# Przy każdym elemenecie pętli
# Tylko dla c=2 3
# Przy każdym elemenecie pętli
# Przy każdym elemenecie pętli
# Przy każdym elemenecie pętli
# Przy każdym elemenecie pętli

imiona = ["Radek", 'Tomek', 'Zenek', "Karolina"]

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Karolina

# 0 Radek
# 1 Tomek...

for i in range(len(imiona)):  # range(4) -> 0123
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Karolina

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Karolina

# enumerate() - zwraca element kolekcji i numer kolejny
for p in enumerate(imiona):
    print(p)
# (0, 'Radek') -> 0 Radek
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Karolina')
a, b = (3, 'Karolina')
print(a, b)  # 3 Karolina

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Karolina

for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Karolina

imiona = ["Radek", 'Tomek', 'Zenek', "Karolina"]
wiek = [44, 55, 32, 27]
for i in range(len(imiona)):
    print(imiona[i], wiek[i])
# Radek 44
# Tomek 55
# Zenek 32
# Karolina 27

imiona = ["Radek", 'Tomek', 'Zenek', "Karolina", "Anna"]
wiek = [44, 55, 32, 27]

# zip() - łączy kolekcje, łaczy tylko pełne dane
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Karolina', 27)
for o, w in zip(imiona, wiek):
    print(o, w)
# Radek 44
# Tomek 55
# Zenek 32
# Karolina 27

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Zenek', 32))
# (3, ('Karolina', 27))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(c, d)  # Radek 44
print(a, c, d)  # 0 Radek 44

# Trzeba wyraźnie za pomocą () wskąząc zmienne, które dotyczą wewnętrznej krotki
(a, (b, c)) = (0, ('Radek', 44))
print(a, b, c)
for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Karolina 27
