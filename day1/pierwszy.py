import sys

print('Hello World')
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
# ctrl d - kopiowanie linii
# ctrl / - komentarz
# print('Radek")
#       C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\.venv\Scripts\python.exe C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\day1\pierwszy.py
#   File "C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\day1\pierwszy.py", line 10
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 10)
#
# Process finished with exit code 1
print("Radek dalej")
print("Radek \"Radek\"")  # Radek "Radek"

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, dane tekstowe

print("39" + '39')  # 3939, konkatenacja, łaczenie tekstów

print(39 + 39)
print(39)
print(type(39))  # <class 'int'>, liczby całkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

# print("39" + 39) # TypeError: can only concatenate str (not "int") to str

# rzutowanie typów, zamiana
print(int("39"))  # rzutowanie int()
print(39 + int("39"))  # 78

print("39" + str(39))  # 3939

# zmienna
# typowanie dynamiczne
name = 90
print(name)
print(type(name))
# print(name + "Kowalski")

name = "Radek"
print(name)
print(type(name))
# 90
# <class 'int'>
# Radek
# <class 'str'>

print(name + "Kowalski")

# podpowiedzi typów
name: str = "Radek"
name = 90
print(name)
# mypy - sprawdzanie typów
#  pip install mypy
# cd .\day1\
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\day1> mypy .\pierwszy.py
# pierwszy.py:52: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# pierwszy.py:60: error: Unsupported operand types for + ("int" and "str")  [operator]
# pierwszy.py:63: error: Name "name" already defined on line 47  [no-redef]
# Found 3 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\day1>
# mypy .\pierwszy.py

print(4 * 'Radek')  # RadekRadekRadekRadek
print(168 * "31")
