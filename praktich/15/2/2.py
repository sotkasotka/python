def count_spaces(text):
    space_count = text.count(" ")
    if space_count % 2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")
input_text = input("Введите строку: ")
count_spaces(input_text)