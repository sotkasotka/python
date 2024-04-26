translit_dict = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'YU', 'Я': 'YA',
}

def transliterate_text(text):
    result = ""
    for char in text:
        if char.upper() in translit_dict:
            if char.isupper():
                result += translit_dict[char.upper()].upper()
            else:
                result += translit_dict[char.upper()].lower()
        else:
            result += char
    return result

text = input("Введите текст для транслитерации: ")

transliterated_text = transliterate_text(text)
print(transliterated_text)
