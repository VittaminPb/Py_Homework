# 33. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

max_value = 100
k = int(input("Введите натуральную степень k: "))

mult = [randint(0, max_value) for i in range(k)] + [randint(1, max_value)]
polynom = "+".join([f'{(j,"")[j==1]}x^{i}' for i,
                   j in enumerate(mult) if j][::-1])

polynom = polynom.replace("x^1+", "x+")
polynom = polynom.replace("x^0", "")
polynom += ("", "1")[polynom[-1] == "+"]
polynom = (polynom, polynom[:-2])[polynom[-2:] == "^1"]
print(f"k={k} => {polynom}=0")

file = open("Task33_file.txt", "w")
file.write(f"{polynom}=0")