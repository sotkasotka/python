n = int(input("Введите количество номеров телефонов: "))

phone_book = {}

for _ in range(n):
    phone, name = input().split()
    phone_book[name] = phone

query_name = input("Введите имя для поиска номера телефона: ")

if query_name in phone_book:
    print(phone_book[query_name])
else:
    print("Нет в телефонной книге")
