import math

x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

def cal_fun(x, y, z):
    frm = (math.sqrt(x**2 + z**2) + 
           math.cos(x * z)**3 + 
           math.sqrt(y**2 + x**2) + 
           math.cos(y * x)**3) / (
           math.sqrt(z**2 + y**2) + 
           math.cos(z * y)**3)
    return frm

pr = cal_fun(x, y, z)
print("Ответ:", pr)