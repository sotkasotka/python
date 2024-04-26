import datetime

def day_ekz(date):
    return date.day % 4 != 0 and date.weekday() != 0

date = input("Введите исходную дату в формате YYYY/MM/DD: ")
year, month, day = map(int, date.split('/'))
date2 = datetime.datetime(year, month, day)

num = int(input("Введите число n: "))

dates = []
while len(dates) < 3:
    if day_ekz(date2):
        dates.append(date2)
    date2 += datetime.timedelta(days=num)

print("Счастливые даты экзаменов:")
for date in dates:
    print(date.strftime("%d %B, %A"))