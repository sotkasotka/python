import datetime

a = int(input("Количество дней до экзамена: "))
b = datetime.datetime.now() + datetime.timedelta(days=a)

print("Дата экзамена:", b.strftime("%d.%m"))