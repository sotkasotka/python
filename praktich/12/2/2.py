n = int(input("Введите размер квадратной матрицы: "))

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Введите элемент [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

print("Исходная квадратная матрица:")
for row in matrix:
    print(row)


negative_sum = 0
for i in range(n):
    for j in range(n):
        if i + j > n - 1 and matrix[i][j] < 0:
            negative_sum += matrix[i][j]

print(f"Сумма отрицательных элементов под дополнительной диагональю: {negative_sum}")
