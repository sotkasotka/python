n = int(input("Введите количество оценок: "))
marks = []
for i in range(n):
    mark = int(input("Введите оценку: "))
    marks.append(mark)
print("Введенные оценки:", marks)
average = sum(marks) / n
print("Средняя оценка за урок:", average)