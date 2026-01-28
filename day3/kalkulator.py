# napisac program kalkulator
# while
# menu z opcjami
# wyświetlec ładnie wynik działania
# obsłużyć wyjątki
# wyswietlic menu -> print
# pobrac opcje -> input
# w zalezności od wyboru wykonac odpowiednią akcję
# if/match
while True:
    print("""
    1.Dodawanie
    2.Odejmowanie
    3.Mnożenie
    4.Dzielenie
    5.Koniec""")

    odp = input("Podaj wybraną opcję")

    # if odp == "5":
    #     break
    if odp not in ["1", "2", "3", "4"]:
        break

    try:
        a = int(input("Podaj pierwsą liczbę:"))
        b = int(input("Podaj drugą liczbę:"))

        if odp == "1":
            print(f"wynik {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"wynik {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"wynik {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"wynik {a} / {b} = {a / b}")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except Exception as e:
        print("Błąd:", e)
    finally:
        print("Operacja wykonana")

wyr = input("Podaj wyrażenie do obliczenia:")
print(eval(wyr))
# Podaj wyrażenie do obliczenia:5*7
# 35
