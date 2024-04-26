import math
def S(r):
    return math.pi * r*2
def l(r):
    return 2 * math.pi * r
def krug():
    radius = float(input("Введите радиус окружности: "))
    print(S(radius), l(radius))
krug()