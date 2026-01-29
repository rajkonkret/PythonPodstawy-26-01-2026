def connect(**opcje):  # dowolna ilość argumentów nazwanych
    print(opcje)


connect()
connect(a=10)
connect(a=10, b=90, c=98, name="Radek", age=90)


# {}
# {'a': 10}
# {'a': 10, 'b': 90, 'c': 98, 'name': 'Radek', 'age': 90}

def all_args(*args, **kwargs):
    print(args, kwargs)


all_args(1, 2, 3, 4, 5, 6, 7, 8)
all_args(1, 2, 3, 4, 5, 6, 7, 8, a=10, b=90)


# (1, 2, 3, 4, 5, 6, 7, 8) {}
# (1, 2, 3, 4, 5, 6, 7, 8) {'a': 10, 'b': 90}

def random_radek(*args, k=0):
    print(args, k)


random_radek(1, 2, 3, 4, 5, k=9)
# k musi byc po nazwie bo jest po *args
# (1, 2, 3, 4, 5) 9
