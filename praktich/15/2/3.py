def print_average(numbers):
    if not numbers: 
        print(0)
    else:
        average = sum(numbers) / len(numbers)
        print(average)
numbers_str = input("Введите числа через пробел: ")
numbers_list = [int(x) for x in numbers_str.split()]
print_average(numbers_list)