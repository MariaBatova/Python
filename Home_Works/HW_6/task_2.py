# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

max_num = int(input("Ведите максимальное число в списке: "))
my_list = [i for i in range(20, (max_num + 1)) if i % 20 == 0 or i % 21 == 0]
print("Список кратный 20 или 21: ", my_list)