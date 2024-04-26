sequence = input("Введите непустую последовательность символов: ")
symbol_set = set()
for char in sequence:
    symbol_set.add(char)
print("Множество символов, встречающихся в последовательности:", symbol_set)
