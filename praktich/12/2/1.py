rows = int(input("Введите количество строк матрицы: "))
cols = int(input("Введите количество столбцов матрицы: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Введите элемент [i][j]: "))
        row.append(element)
    matrix.append(row)
    print("Исходная матрица:")
for row in matrix:
    print(row)
    sums = [0] * cols
for i in range(rows):
    for j in range(cols):
        sums[j] += matrix[i][j]
print("Суммы элементов каждого столбца:")
for j in range(cols):
    print(f"Сумма элементов столбца", sums[j])