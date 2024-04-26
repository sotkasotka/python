string = "Привет мир"

a = string.split()[::-1]
b = []
for i in a:
    b.append(i)
print(" ".join(b))
