import csv

# filename = "records.csv"
filename = "records_discount.csv"

fields = []
rows = []

with open(filename, "r") as csv_f:

    csvreadder = csv.reader(csv_f, delimiter=";")
    print(csvreadder)
    # <_csv.reader object at 0x0000022F01E2BA00> - iterator

    fields = next(csvreadder) # odczyt pierwszego wiersz z danych

    for row in csvreadder: # zaczyna od drugiego wiersza
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]

# Fields: ['sku;exp_date;price']
# Rows: [['1;today;200'], ['2;today;100'], ['3;tomorrow;500'], ['4;today;2000'], ['5;today;1200'], ['6;tomorrow;700']]
# Fields: ['sku', 'exp_date', 'price']