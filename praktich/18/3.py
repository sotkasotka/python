import module
list_a = [None] * int(input("Введите количество элементов списка: "))
num_elements = int(input("Сколько элементов списка следует заполнить: "))
value = int(input("Введите значение для заполнения элементов: "))
filled_list = module.fill_list(list_a, num_elements, value)
print("Заполненный список:", filled_list)