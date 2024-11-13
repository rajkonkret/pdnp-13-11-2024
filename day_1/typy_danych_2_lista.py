# Kolekcje
# lista - przechowuje wiele elementów, różnego typu na raz

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodawanie elemntów na końcu listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Adam")
lista.append("Marek")
lista.append("Zenek")
lista.append("Anna")
print(lista)  # ['Radek', 'Tomek', 'Adam', 'Marek', 'Zenek', 'Anna']

# ['Radek', 'Tomek', 'Adam', 'Marek', 'Zenek', 'Anna']
#     0        1       2        3        4        5   - indeksy w liście
#     -6       -5     -4       -3        -2       -1
print(lista[0])  # Radek
print(lista[2])  # Adam
print(lista[4])  # Zenek

# print(lista[10]) # IndexError: list index out of range
print(len(lista))  # 6
print(lista[len(lista) - 1])  # Anna, ostatni element listy
print(lista[-1])  # Anna, ostatni element listy
print(lista[-2])  # Zenek
print(lista[-6])  # Radek

# ['Radek', 'Tomek', 'Adam', 'Marek', 'Zenek', 'Anna']
#     0        1       2        3        4        5   - indeksy w liście
#     -6       -5     -4       -3        -2       -1
# wyświetlanie fragmentów listy, slicowanie
print(lista[0:3])  # ['Radek', 'Tomek', 'Adam'] 012, indeks 3 nie jest brany pod uwagę
print(lista[:3])  # ['Radek', 'Tomek', 'Adam']
print(lista[2:])  # ['Adam', 'Marek', 'Zenek', 'Anna']
print(lista[2:5])  # ['Adam', 'Marek', 'Zenek']

print(lista[:])  # ['Radek', 'Tomek', 'Adam', 'Marek', 'Zenek', 'Anna']
print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Adam', 'Marek'] -> [0:4]

print(lista[2:3])  # ['Adam']
print(lista[2:2])  # []

print(lista[2:10])  # ['Adam', 'Marek', 'Zenek', 'Anna']
print(lista[10:29])  # []

lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:10:2])  # [0, 2, 4, 6, 8]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14], [start:stop:step]
print(lista_15[-10])  # 5

# nadpisanie elementu w liście
lista[3] = "Mikołaj"
print(lista)  # ['Radek', 'Tomek', 'Adam', 'Mikołaj', 'Zenek', 'Anna']
print(len(lista))  # długość 6

# wstawienie we wskazane miejsce
lista.insert(1, "Karolina")
print(lista)  # ['Radek', 'Karolina', 'Tomek', 'Adam', 'Mikołaj', 'Zenek', 'Anna']
print(len(lista))  # 7

# sprawdzenie indeksu
print(lista.index('Karolina'))  # indeks numer 1

lista.append("Mikołaj")
print(lista)  # ['Radek', 'Karolina', 'Tomek', 'Adam', 'Mikołaj', 'Zenek', 'Anna', 'Mikołaj']
print(lista.index("Mikołaj"))  # pierwszy napotkany indeks, 4

# usuniecie z listy, pierwszy napotkany
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Karolina', 'Tomek', 'Adam', 'Zenek', 'Anna', 'Mikołaj']

# usunięcie po indeksie
print(lista.pop(4))  # Zenek - pokazuje kogo usunął
print(lista)  # ['Radek', 'Karolina', 'Tomek', 'Adam', 'Anna', 'Mikołaj']

a = 1
b = 3
a = b
print(a, b)  # 3,3
b = 7
print(a, b)  # 3 7

lista_2 = lista  # a = b, kopia referencji, kopia adresu w pamięci
lista_copy = lista.copy()  # kopia elementów listy
print(lista_2, lista)
# ['Radek', 'Karolina', 'Tomek', 'Adam', 'Anna', 'Mikołaj'] ['Radek', 'Karolina', 'Tomek', 'Adam', 'Anna', 'Mikołaj']
lista.clear()  # czyszczenie elementów listy
print(lista_2, lista)  # [] []
print(lista_copy)
print(id(lista))  # 1361554350592
print(id(lista_2))  # 1361554350592
print(id(lista_copy))  # 1993276194304
