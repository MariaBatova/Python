# 1. Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.

# -------------------------------------- 1 вариант

# num = int(input())
# result = 1

# for i in range(num):
#     print(result, end=", ")
#     result *= -3


# -------------------------------------- 2 вариант

num = int(input())

for i in range(num):
    print((-3) ** i, end=", ")