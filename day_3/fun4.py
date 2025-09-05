def connect(**opcje):  # dowolna ilość argumentów nazwanych - kwargs
    print(opcje)


connect()  # {} - słownik
connect(a=7)  # {'a': 7}


def all_args(*args, **kwargs):
    print(f"{args=}")
    print(f"{kwargs=}")


all_args(1, 2, 3)
all_args(a=8, b=9)
all_args(1, 2, v=90)
# ---
# args=(1, 2, 3)
# kwargs={}
# ---
# args=()
# kwargs={'a': 8, 'b': 9}
# ----
# args=(1, 2)
# kwargs={'v': 90}
