# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math

num = int(input())
list = []
i = 2

while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
        i = 2
    else:
        i += 1

print(list)