a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # użyj zmiennej globalnej
    a = 7
    b = 90
    print(a + b)


print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 10 (globalna)
dodaj()  # 15
print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 10 (globalna)
dodaj2()  # 20
print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 10 (globalna)
dodaj3()  # 97
print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 7 (globalna)
dodaj2()  # 17
