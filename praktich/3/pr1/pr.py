a = int(input("Введите число А: "))
b = int(input("Введите число Б: "))
if a % b == 0: 
    print('делится') 
else: 
    print('не делится, остаток', a % b) 
    print(a / b)