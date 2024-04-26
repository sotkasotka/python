k = int(input('Количество чисел: '))

negatives = 0
for _ in range(k):
    num = int(input(f'Введите {_+1}-е число: '))
    if num < 0:
        negatives += 1

print(f'Вы ввели {negatives} отрицательных чисел')