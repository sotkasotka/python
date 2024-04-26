n = int(input("Введите количество студентов: "))

students_dict = {}

for _ in range(n):
    surname, specialty, group = input().split()
    if specialty in students_dict:
        students_dict[specialty].append(surname)
    else:
        students_dict[specialty] = [surname]

query_specialty = input("Введите название специальности: ")

if query_specialty in students_dict:
    print(", ".join(students_dict[query_specialty]))
else:
    print("Проверьте запрос")
