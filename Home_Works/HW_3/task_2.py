# 2. Напишите программу, которая найдёт произведение пар чисел списка.
#    Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def list_random(count):
    if count < 0:
        print("Error!")
        return []

    list_num = sample(range(1, count * 2), count)
    return list_num
 
def list_2(list_nums):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):
        res_list.append(list_nums[k] * list_nums[len_list - k - 1])

    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list


all_list = list_random(int(input("Number of numbers: ")))
print(all_list)
print(list_2(all_list))