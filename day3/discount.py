from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2026-01-28
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2026-01-28 14:56:11.808202

print(today.day)  # 28

formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 28/01/2026
print(type(formated_date))  # <class 'str'>

formated_time = datetime.now().strftime("%H:%M:%S")
print(formated_time)  # 14:59:33
print(type(formated_time))  # <class 'str'>

object_data = datetime.now().strptime("28/01/2026", "%d/%m/%Y")
print(object_data)  # 2026-01-28 00:00:00
print(type(object_data))  # <class 'datetime.datetime'>

#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2026-01-29

products = [
    {"sku": 1, "exp_date": today, "price": 200},
    {"sku": 2, "exp_date": today, "price": 100},
    {"sku": 3, "exp_date": tomorrow, "price": 500},
    {"sku": 4, "exp_date": today, "price": 2000},
    {"sku": 5, "exp_date": today, "price": 1200},
    {"sku": 6, "exp_date": tomorrow, "price": 700},
]

for p in products:
    print(p['exp_date'])
    if p['exp_date'] != today:
        continue  # kończy dziłanie z bieżącym elementem pętli
    p['price'] *= 0.8  # p = p * 0.8
    print(f"""
Price for sku {p['sku']}
is now: {p['price']:.2f}""")
# Price for sku 1
# is now: 160.00
# 2026-01-28
#
# Price for sku 2
# is now: 80.00
# 2026-01-29
# 2026-01-28
#
# Price for sku 4
# is now: 1600.00
# 2026-01-28
#
# Price for sku 5
# is now: 960.00
# 2026-01-29