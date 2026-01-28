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
