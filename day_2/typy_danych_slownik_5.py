# słownik - para klucz-wartosc
# {"user":"Radek"}
# klucze nie mogą powtarzać
# odpowiednik jsona

# pusty słownik
dictionary = {}
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

pusty_zbior = dict()
print(type(pusty_zbior))  # <class 'dict'>
print(pusty_zbior)  # {}

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 50
print(dictionary)  # {'imie': 'Radek', 'wiek': 50}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 50])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 50)])

dict_list = {'imie': ["Radek", "Tomek", "Zenek"]}
print(dict_list)  # {'imie': ['Radek', 'Tomek', 'Zenek']}

# wypisanie wartości
print(dictionary['imie'])  # Radek
print(dict_list['imie'])  # ['Radek', 'Tomek', 'Zenek']
print(dict_list['imie'][1])  # Tomek

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary["Imie".lower()])  # Radek

print(dictionary.get('imie'))  # Radek
print(dictionary.get('Imie'))  # None
print(dictionary.get('Imie', "default"))  # default, wartosc domyslna

dictionary.update({'data': "31-12-2027"})
print(dictionary)  # {'imie': 'Radek', 'wiek': 50, 'data': '31-12-2027'}

# input() - wprowadzanie danych np.:  z kalwiatury
tekst = input("Podaj imię")
print(tekst)
# Podaj imięRadek
# Radek
