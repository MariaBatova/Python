# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def list_random(count):
    if count < 0:
        print("Error!")
        return []

    list_num = sample(range(1, count * 2), count)
    return list_num

def sum_el(list_num):
    sum_num = 0
    for k in range(0, len(list_num), 2):
        sum_num += list_num[k]
    return sum_num

all_list = list_random(int(input("Number of numbers: ")))
print(all_list)
print(sum_el(all_list))
