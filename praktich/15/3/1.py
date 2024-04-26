def process_list(numbers, criteria):
    a, b, c = criteria
    matching_elements = []
    sum_of_others = 0
    for num in numbers:
        if a < num < b and num % c == 0:
            matching_elements.append(num)
        else:
            sum_of_others += num
    print("Элементы, удовлетворяющие условиям:", matching_elements)
    print("Сумма остальных элементов:", sum_of_others)
numbers = [1, 5, 12, 20, 33, 45, 51]
criteria = [5, 40, 3]
process_list(numbers, criteria)