s = input('Введите предложение: ')

if not s.endswith('.'):
    print('Строка не оканчивается точкой!')

print(f'Кол-во слов: {len(s.split(" "))}')