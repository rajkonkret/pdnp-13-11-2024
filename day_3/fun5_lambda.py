# funkcja lambda
# skrócony zapis funkcji
# funkcja anonimowa, mozliwosc uzycia w miejscu deklaracji
# lambda zwraca wynik (ma return)

def odejmij(a, b):
    return a - b


print(odejmij(5, 9))

odejmij2 = lambda a, b: a - b
print(odejmij2(4, 90))

# mapowanie danych
lista = [1, 2, 3, 10, 20, 50, 70, 200, 300, 500]
lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)

print(lista_wyn)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]


def zmien(x):
    return x * 2


lista_wyn2 = []
for i in lista:
    lista_wyn2.append(zmien(i))

print(lista_wyn2)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
# funkcje wyzszego rzedu
# map() - pobiera dane i wykonuje na nich funkcje
print(f"Zastosowanie map() {list(map(zmien, lista))}")  # Zastosowanie map() [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
print(
    f"Zastosowanie map() {list(map(lambda x: x * 2, lista))}")  # Zastosowanie map() [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
print(
    f"Zastosowanie map() {list(map(lambda x: x * 4, lista))}")  # Zastosowanie map() [4, 8, 12, 40, 80, 200, 280, 800, 1200, 2000]
print(
    f"Zastosowanie map() {list(map(lambda x: x * 5, lista))}")  # Zastosowanie map() Zastosowanie map() [5, 10, 15, 50, 100, 250, 350, 1000, 1500, 2500]

# filtrowanie danych
# filter() zwraca elementy spełniające warunek
print(f"Zastosowanie filter() {list(filter(lambda x: x < 5, lista))}")  # Zastosowanie filter() [1, 2, 3]
print(f"Zastosowanie filter() {list(filter(lambda x: x > 50, lista))}")  # Zastosowanie filter() [70, 200, 300, 500]
print(f"Zastosowanie filter() {list(filter(lambda x: x > 3 and x < 20, lista))}")  # Zastosowanie filter() [10]
print(f"Zastosowanie filter() {list(filter(lambda x: 3 < x < 20, lista))}")  # Zastosowanie filter() [10]
