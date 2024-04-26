print("Введите слова, которые начинаются на букву 'с' (заглавную или строчную):")
while True:
    word = input("Введите слово: ")
    if word.lower().startswith('с'):
        print(word)
    else:
        break   