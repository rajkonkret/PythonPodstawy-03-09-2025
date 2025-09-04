# od python 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.strip().casefold():
    case "python":
        lista.append("Znam pythona")
    case "java":
        lista.append("Znam jave")
    case _:  # odpowiednik else
        print("Inny")

print(lista)  # ['Znam jave']
