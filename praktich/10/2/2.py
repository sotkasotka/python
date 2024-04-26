s = input("Введите непустую последовательность символов: ")
symbols = 'EFGHIJKLMNefghijkl!,.:;?'
print ({s[i] for i in range(len(s)) if s[i] in symbols})