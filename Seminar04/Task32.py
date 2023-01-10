# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

list = [randint(0, 10) for i in range(randint(10, 15))]
print(list)

non_repet = [i for i in list if list.count(i)==1]
print(non_repet)