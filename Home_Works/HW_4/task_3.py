# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
#    неповторяющихся элементов исходной последовательности в том же порядке.

res = []
lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")

for i in lst:
    if lst.count(i) == 1:
        res += [i] 

print(res)
