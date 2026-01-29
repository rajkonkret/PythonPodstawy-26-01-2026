# stworzyc funkcję kantor
# ma mieć dwie wewnętrzne funkcje: eur, usd
# w zależności od parametrów ma zwrócić jedną z funkcji
# przekazanie kwoty do funkcji usd, eur

def kantor(waluta):
    print("Otwieram Kantor")

    def usd(kwota):
        print(f"Wymieniam: {kwota} usd na: {kwota * 3.52}  pln")

    def eur(kwota):
        print(f"Wymieniam: {kwota} eur na: {kwota * 4.21}  pln")

    if waluta == "eur":
        return eur
    else:
        return usd

kantor_usd = kantor("usd")
kantor_usd(1000)
# Wymieniam: 1000 usd na: 3520.0  pln

kantor_eur = kantor("eur")
kantor_eur(45567) # Wymieniam: 45567 eur na: 191837.07  pln

kantor_usd(678)
# Wymieniam: 678 usd na: 2386.56  pln