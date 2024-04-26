def filter_even_above_10(numbers):
    filtered_list = [num for num in numbers if num % 2 == 0 and num > 10]
    return filtered_list
numbers_str = input("Введите числа через пробел: ")
numbers_list = [int(x) for x in numbers_str.split()]
result = filter_even_above_10(numbers_list)
print(result)