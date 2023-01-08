# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = list(map(float, input("Введите числа через пробел: ").split()))

diff_max_min = [round(i % 1, 2) for i in n if i % 1 != 0]
print(max(diff_max_min) - min(diff_max_min))