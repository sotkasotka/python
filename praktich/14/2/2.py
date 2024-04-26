n = int(input("Введите количество специальностей: "))

specialties_dict = {}

for _ in range(n):
    specialty_info = input().split(" - ")
    specialty_name = specialty_info[0]
    groups = list(map(int, specialty_info[1].split(", ")))

    specialties_dict[specialty_name] = groups

query_group = int(input("Введите номер группы: "))

found_specialty = None
for specialty, groups in specialties_dict.items():
    if query_group in groups:
        found_specialty = specialty
        break

if found_specialty:
    print(found_specialty)
else:
    print("")
