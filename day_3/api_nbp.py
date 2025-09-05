import requests

# pip install requests -  w terminalu


url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

response = requests.get(url)
print(response)  # <Response [200]>
# 2xx - ok, 200
# 3xx - warningi, przekierowanie
# 4xx - 404 - brak zasobu, 400 Bad Request - bledne zapytanie
# 5xx - Intenal server errror 500

print(response.text)
# {"table":"A","currency":"euro","code":"EUR","rates":[{"no":"172/A/NBP/2025","effectiveDate":"2025-09-05","mid":4.2476}]}
print(type(response.text))  # <class 'str'>

data = response.json()
print(type(data))  # <class 'dict'>
print(data)

print(data.keys())  # dict_keys(['table', 'currency', 'code', 'rates'])
for i in data:
    print(i)
# table
# currency
# code
# rates
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '172/A/NBP/2025', 'effectiveDate': '2025-09-05', 'mid': 4.2476}]}

print(data['rates'])
# [{'no': '172/A/NBP/2025', 'effectiveDate': '2025-09-05', 'mid': 4.2476}]
print(data['rates'][0])  # {'no': '172/A/NBP/2025', 'effectiveDate': '2025-09-05', 'mid': 4.2476}
# ze słownika odczytujemy po kluczu
print(data['rates'][0]['mid'])  # 4.2476
