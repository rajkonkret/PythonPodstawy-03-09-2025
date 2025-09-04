# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat1")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break

print(licznik)

licznik = 0  # muszę licznik zzerowac
while licznik < 10:
    licznik += 1
    print("komunikat 3 !!!")

# password = input("Podaj hasło")
# while password != "secret":
#     password = input("Błedne hasło. Podaj ponownie")
#
# print("hasło prawidłowe")
# Podaj hasłoq
# Błedne hasło. Podaj ponowniea
# Błedne hasło. Podaj ponownie1
# Błedne hasło. Podaj ponownieerert
# Błedne hasło. Podaj ponowniewerwrw
# Błedne hasło. Podaj ponowniesecret
# hasło prawidłowe


# lista = []
# lista_int = []
# while True:
#     wej = input("Podaj liczbę")  # str
#     # A string is numeric if all characters in the string are numeric
#     if not wej.isnumeric(): # wpisanie literki przerywa pętle
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))
#
# print(lista)  # ['1', '2', '3', '4', '5']
# print(lista_int)  # [1, 2, 3, 4, 5] - lista intów

# uunie wszystkie wystapienia liczby 5
my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
while 5 in my_list:
    my_list.remove(5)
print(my_list)  # [1, 2, 3, 4, 6]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}
unique_numbers = list(dict.fromkeys(my_list))
print(unique_numbers)  # [1, 5, 2, 3, 4, 6], bez utraty kolejności
