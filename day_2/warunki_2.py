# od pythona 3.10
# match case

lista = []
lang = input("Podaj znay Ci język programowania")

match lang.casefold().strip():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam Javę")
    case _:  # odpowiednik else, domyślne działanie
        print("Nie znam takiego języka")

print(lista)  # ['Znam Javę']