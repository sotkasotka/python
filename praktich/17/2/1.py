import random

e = int(input("Количество экзаменов: "))

o = input("Введите названия дисциплин через запятую и пробел: ").split(", ")

d = ["понедельник", "вторник", "среда", "четверг", "пятница"]
v = [9.0 + 0.5 * i for i in range(10)]

for i in range(e):
    dd = random.choice(d)
    tt = random.choice(v)
    ran = random.randint(1, 20)
    print(f"Экзамен по дисциплине «{o[i]}» состоится в {dd} время {tt:.1f}. Ваш счастливый билет N# {ran}.")