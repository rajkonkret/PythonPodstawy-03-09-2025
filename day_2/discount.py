from copyreg import dispatch_table
from datetime import datetime, date, timedelta

today = date.today()
print(today)  # 2025-09-04
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2025-09-04 14:58:57.290594

print(time.year)
print(today.day)
# 2025
# 4

# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2025-09-05

formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 04/09/2025 -> str

formated_time = datetime.now().strftime("%H:%M")
print(formated_time)  # 15:03

# z daty w stringu otrzymalismy obiekt datetime
object_time = datetime.now().strptime("04/09/2025", "%d/%m/%Y")
print(object_time)  # 2025-09-04 00:00:00
print(type(object_time))  # <class 'datetime.datetime'>
