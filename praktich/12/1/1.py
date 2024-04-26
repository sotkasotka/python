strok = int(input("Введите количество строк в матрице: "))
stolb = int(input("Введите количество столбцов в матрице: "))

matrix = []
print("Введите элементы матрицы:")
for i in range(strok):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(strok):
    if i % 2 == 0:
        print(*matrix[i])
    else:
        print(*matrix[i][::-1])