kz1 = set(map(int, input("Введите элементы первого множества: ").split()))
kz2 = set(map(int, input("Введите элементы второго множества: ").split()))

unique_numbers = kz1.union(kz2)

common_numbers = sorted(kz1.intersection(kz2))

print("Различные числа в двух множествах:", unique_numbers)
print("Числа, которые входят как в первое, так и во второе множества в порядке возрастания:", common_numbers)