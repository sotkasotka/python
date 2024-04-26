def fakt(x):
    if x == 0:
        return 1
    else:
        return x * fakt(x - 1)
def fun(x, y):
    result = fakt(x) / (fakt(y) * fakt(x - y))
    return result
x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = fun(x, y)
print("Ответ:", z)