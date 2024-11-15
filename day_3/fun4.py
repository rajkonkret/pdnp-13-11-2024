# zrobic funkcje obliczającą średnią
def liczymy(name=None, *opcje):  # * - dowolna ilośc argumentów przekazanych pozycyjnie
    print(opcje)
    count = len(opcje)
    suma_p = sum(opcje)
    suma = 0
    try:
        for c in opcje:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia ucznia {name} wynosi {avg}")
    finally:
        print("Kolejny uczeń")


liczymy()  # ()
# name, *opcje = "Radek", 1, 2, 4, 4, 5, 5
liczymy("Radek", 5, 5, 6, 6, 5)


# ()
# Bład division by zero
# Kolejny uczeń
# (5, 5, 6, 6, 5)
# Średnia ucznia Radek wynosi 5.4
# Kolejny uczeń

#
def nazwane(**kwargs):  # ** dowolna ilosc argumentów nazwanych
    print(kwargs)


nazwane(a=8, n=90, name="Radek")  # {'a': 8, 'n': 90, 'name': 'Radek'}


def funkcja(*args, **kwargs):
    print(args, kwargs)


funkcja(1, 2, 3, z=90)  # (1, 2, 3) {'z': 90}
