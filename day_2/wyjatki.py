# wyjątek - błąd podczas wykonywania programu

# print(5 / 0) # ZeroDivisionError: division by zero

print("Dalsza częśc programu")

try:
    # print(5 / 0)
    # print("a" * "23")
    # print(int("A"))
    raise KeyError("Brak klucza")
    value = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez 0")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład:", e)
else:
    print("Wartość:", value)
finally:  # wykona się niezależnie od tego czy błąd wystąpi czy nie
    print("wykona się zawsze")
print("Dalsza częśc programu")
# Dalsza częśc programu
# Bład: 'Brak klucza'
# Dalsza częśc programu
# Dalsza częśc programu
# Wartość: 30.0
# Dalsza częśc programu
