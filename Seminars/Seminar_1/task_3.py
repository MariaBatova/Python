# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# -------------------------------------- 1 вариант

num = int(input("Введите число: "))
print(*range(-num, num + 1))
    
# -------------------------------------- 2 вариант

num = int(input("введите число: "))
if num > 0:
    print(*range(-num, num + 1))
else:
    print(*range(-num, num - 1, -1))


# -------------------------------------- 3 вариант

num = int(input())
neg_num = -num
print(neg_num, end=", ")

while num != neg_num:
    if num > 0:
        neg_num += 1
    else:
        neg_num -= 1
    print(neg_num, end=", ")