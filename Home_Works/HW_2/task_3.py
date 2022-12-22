# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

num = int(input())
num_list = []
sum = 0

for i in range(1, num + 1):
    res = round((1 + 1 / i) ** i, 3)
    num_list.append(res)
    sum += res

print(num_list)
print(sum)