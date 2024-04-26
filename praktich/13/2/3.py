def sum_subsequence(numbers, start, end):

   
    if start < 0 or end >= len(numbers) or start > end:
        return "Ошибка: некорректные индексы."

    return sum(numbers[start:end+1]) 

numbers_str = input("Введите числа через пробел: ")
x, y = map(int, input("Введите начальный и конечный индексы (X Y): ").split())


numbers_list = [int(x) for x in numbers_str.split()]


result = sum_subsequence(numbers_list, x, y)
print(result)