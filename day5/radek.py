"""
Plik radek.py
Prosty moduł z funkcją przywitania oraz funkcjami sumy i średniej od 1 do n.
"""

from typing import Union


def przywitaj(imie: str) -> str:
    """Zwraca powitanie dla podanego imienia."""
    return f"Cześć, {imie}!"


def suma_do(n: int) -> int:
    """Zwraca sumę liczb od 1 do n (n >= 0)."""
    if n < 0:
        raise ValueError("n musi być >= 0")
    return n * (n + 1) // 2


def srednia_do(n: int) -> float:
    """Zwraca średnią liczb od 1 do n (n > 0)."""
    if n <= 0:
        raise ValueError("n musi być > 0")
    return suma_do(n) / n


if __name__ == "__main__":
    import sys

    # Przywitanie — imię z argumentu CLI lub z wejścia
    imie = sys.argv[1] if len(sys.argv) > 1 else input("Podaj imię: ")
    print(przywitaj(imie))

    # Krótkie demo funkcji suma_do i srednia_do
    n = 10
    print(f"Suma od 1 do {n} = {suma_do(n)}")
    print(f"Średnia od 1 do {n} = {srednia_do(n)}")
