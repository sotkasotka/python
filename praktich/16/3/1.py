def fed(qu):
    return qu % 8 == 0 and 100 <= qu <= 999
xyz = sum(num**3 for num in range(100, 1000) if fed(num))
text = "Сумма кубов всех трехзначных чисел, % 8:"
print(text, xyz)