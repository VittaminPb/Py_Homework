# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random 
n = int(input("Введите число N: "))
rndList = []
for i in range(n):
    rndList.append(random.randint(-n, n)) 
print(rndList)
 
a = open("file.txt")
print(rndList[int(a.readline())] * rndList[int(a.readline(2))])