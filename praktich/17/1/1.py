import string
import random

def pas(N, l):
    pass_2 = set()
    while len(pass_2) < N:
        pass_2.add(passw(l))
    return pass_2

def passw(length):
    char = string.ascii_letters + string.digits
    password = ''.join(random.choice(char) for _ in range(length))
    return password

N = int(input("Количество паролей: "))
l = int(input("Длина пароля: "))

passwords = pas(N, l)
for password in passwords:
    print(password)