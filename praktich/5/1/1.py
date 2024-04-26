x = int(input())
y = [x]
while x != 0:
    x = int(input())
    y.append(x)
for z in reversed (y):
    print(z)