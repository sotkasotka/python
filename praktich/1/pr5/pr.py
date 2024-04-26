print("Стоимость пирожка:")
rub = int(input("рублей: "))
kop = int(input("Копеек: "))
print("Колличество пирожков")
pie = int(input())
price = rub * 100 + kop
summa = price * pie
price_rub = summa // 100
price_kop = summa % 100
print(price_rub, "рублей" , price_kop, "копеек")