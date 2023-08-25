# Dates

from datetime import datetime

now = datetime.now()

def print_date(date):

    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)

year2024 = datetime( 2024, 1, 1)

print_date(year2024)

from datetime import time

current_time = time(11, 3, 3)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(2005, 8, 28)

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(current_date.year - 10, current_date.month + 1, current_date.day)

print(current_date)

diff = year2024 - now
print(diff)
diff = year2024.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_tiemedelta = timedelta(300, 100, 100, weeks = 13)

print(end_tiemedelta - start_timedelta)
print(end_tiemedelta + start_timedelta)
