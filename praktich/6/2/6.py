import math
k = 3
b = [k]
for a in range(1002, 9999, k):
    b.append(a)
    print("Сумма равна: ", sum(b))