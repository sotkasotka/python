def separate_and_capitalize(text):


    words = text.upper().split() 
    separated_words = ["-".join(word) for word in words]
    return " ".join(separated_words)  

input_text = input("Введите строку с словами: ")
result = separate_and_capitalize(input_text)
print(result)