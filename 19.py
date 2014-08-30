import datetime as dt

date = dt.date(1901, 1, 1)
day = dt.timedelta(days=1)
count = 0
while True:
    if date.isoweekday() == 7 and date.day == 1:
        count += 1
    if date >= dt.date(2000, 12, 31):
        break
    date += day
print(count)