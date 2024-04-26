def max_letter_count(text):

    letter_counts = {}  
    for char in text.lower():
        if char.isalpha():  
            letter_counts[char] = letter_counts.get(char, 0) + 1

    if letter_counts:  
        return max(letter_counts.values())
    else:
        return 0  

input_text = input("Введите строку: ")
result = max_letter_count(input_text)
print(result)