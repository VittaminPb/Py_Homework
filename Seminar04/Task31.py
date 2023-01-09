# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math

n = int(input("Введите натуральное число: "))
print(f"простые множители числа {n}: ", end="")

while n % 2 == 0:
    print(2, end=" "),
    n = n / 2

for i in range(3, int(math.sqrt(n))+1, 2):

    while (n % i == 0):
        print(i, end=" ")
        n = int(n / i)
if n > 2:
    print(n)
