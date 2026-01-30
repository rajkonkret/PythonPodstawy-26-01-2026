# dekorator
# przyjmuje inną funkcja jako argument
# wykorzystuje konstrukcje funkcji wew

from colorama import init, Fore, Style

# pip install colorama

init(autoreset=True)


def dekor(fun):
    def wew():
        print("Dodatkowe działanie")
        return fun()  # uruchamiamy funkcje dekorowaną

    return wew  # zwracamy referencje, adres funkcj wew


@dekor
def hej():
    print("Hej!!!")


hej()


# Hej!!!
# po dodaniu dekoratora @dekor
# Dodatkowe działanie
# Hej!!!
def color_decorator(fun):
    def wrapper():
        result = fun()
        return Fore.RED + result + Style.RESET_ALL

    return wrapper


@color_decorator
def napis():
    return "HELLO WORLD!"


print(napis())  # HELLO WORLD!
