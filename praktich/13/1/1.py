def rearrange_sentence(numbers, words):

    word_list = words.split()
    index_list = [int(x) - 1 for x in numbers.split()]

    
    if any(index < 0 or index >= len(word_list) for index in index_list):
        return "Ошибка: некорректные номера слов."

    new_sentence = ' '.join(word_list[i] for i in index_list)
    return new_sentence.capitalize()


numbers_str = input("Введите номера слов через пробел: ")
words_str = input("Введите слова через пробел: ")
result = rearrange_sentence(numbers_str, words_str)
print(result)