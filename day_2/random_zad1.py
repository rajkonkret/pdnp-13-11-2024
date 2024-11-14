import random

from day_1.typy_danych_2_lista import lista_2

# wspomaga generowanie liczb pseudolosowych

print(random.randint(1, 100))  # int od 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4
print(random.random())  # float 0.7022342000622032 od 0 do 0.99999999
print(random.random() * 15)  # float 9.52054671685948 od 0 do 14.99999999

lista = [67, 45, 32, 68, 69, 90]
print(type(lista))  # <class 'list'>
print(random.choice(lista))  # 90

lista_kule = list(range(1, 50))  # od 1 do 49
print(lista_kule)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
# 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

# moglibyśmy to 6 razy wykonać
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # [26, 14, 7, 42, 14, 35], losuje powtarzające się
print(random.sample(lista_kule, k=6))  # losuje bez powtórzeń
print(random.sample(lista_kule, 6))
# [46, 39, 45, 29, 9, 42]
# [16, 2, 15, 18, 38, 6]
