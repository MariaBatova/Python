# 1. Вычислить число c заданной точностью d.

from decimal import *

num = Decimal(input("Enter a real number: "))
print(num.quantize(Decimal(input("Enter the required accuracy '0.0001': "))))
