import math
a = 1.5
p = 3.14
x = float(input("Введите число x: "))
if x < 1.3:
    print(p * x**2 - 7 / x**2)
elif x == 1.3:
    print(a * x**3 + 7 * math.sqrt(x))
elif x > 1.3:
    print(math.log10(x + 7 * math.sqrt(x)))