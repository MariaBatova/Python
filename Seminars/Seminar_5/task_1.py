# 1. Создайте список из N натуральных чисел(0 до N),
#    упорядоченных по возрастанию. Среди чисел не хватает
#    одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
#    Найдите это число.

from random import choice;

def make_list():
    num = int(input("Input your number, please: "))
    Is = [i for i in range(num + 1)]
    Is.remove(choice(Is))
    print(Is)
    return Is

def find_num(lst):
    for i in range(1, len(lst)):
        if lst[i] - 1 != lst[i - 1]:
            return lst[i] - 1
    return - 1 

print(find_num(make_list()))