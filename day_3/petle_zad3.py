# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("komunikat 1 !")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break

print(licznik)
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# 11
licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!

# password = input("Podaj hasło")
# while password != 'secret':
#     password = input("Błędne hasło. Podaj ponownie")
#
# print("Hasło prawidłowe")
# Podaj hasłoffsgsg
# Błędne hasło. Podaj ponownieeeww
# Błędne hasło. Podaj ponownieewrwerwe
# Błędne hasło. Podaj ponowniess
# Błędne hasło. Podaj ponownieaada
# Błędne hasło. Podaj ponownie222
# Błędne hasło. Podaj ponownie22fsf
# Błędne hasło. Podaj ponowniesecret
# Hasło prawidłowe

# pętla while True często jest stosowana jako głowna pętla programu
lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)
# ['5', '6', '23', '123', '890'] str
# [5, 6, 23, 123, 890] int
# A string is numeric if all characters in the string are numeric

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
while 5 in my_list:
    my_list.remove(5)

# nie zmienilismy kolejnosci
print(my_list)  # [1, 2, 3, 4, 6]
