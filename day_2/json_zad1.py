import json

person_dict = {'name': "Radek", 'age': 40, "czy_pali": None}
with open("nasze_dane.json", "w") as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

with open("nasze_dane.json", "w") as f:
    json.dump(person_dict, f, indent=True)
# {
#  "name": "Radek",
#  "age": 40,
#  "czy_pali": null
# }

with open("nasze_dane.json", "r") as file:
    data = json.load(file)

print(data)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(data))  # <class 'dict'>

print(data['age'])  # 40

json_text = json.dumps(data)
print(type(json_text))  # <class 'str'>
print(json_text)  # {"name": "Radek", "age": 40, "czy_pali": null}

dict_json = json.loads(json_text)
print(dict_json)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(dict_json))  # <class 'dict'>
