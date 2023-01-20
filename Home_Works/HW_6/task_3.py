# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

# name_list = input("Введите списко имён: ")
# print (name_list.split())
name_list = "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
print(name_list)

name_dict = {}

for name in name_list:
    key = name[0]

    if key not in name_dict:
        name_dict[key] = []
    name_dict[key].append(name)

print (name_dict)