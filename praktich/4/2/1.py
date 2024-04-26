import math
a = -0.5
b = 2
t = float(input("Введите число t: "))
e = int(input("Введите число e: "))
if 1 <= t <= 2:
    print((a * t**2 * math.log(10) * t))
elif t < 1:
    print(1)
elif t > 2:
    print(e**(a*t) * math.cos(b * t))