rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Введите элемент [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

min_element = matrix[0][0]
min_row = 0
min_col = 0

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]
            min_row = i
            min_col = j

print(f"Минимальный элемент матрицы: {min_element}")
print(f"Индексы минимального элемента: [{min_row}][{min_col}]")
