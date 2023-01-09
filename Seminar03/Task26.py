# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input("Введите целое число: "))

# a = b = 1
# print(0, a, b, end = " ")

# i = 2
# while i < n:
# 	a, b = b, a + b
# 	print(b, end = " ")
# 	i += 1

def positive_fib(n):

	postive_list = [0, 1]
	for i in range(n-1):
		postive_list.append(postive_list[-2]+postive_list[-1])
	return postive_list


def negative_fiv(n):

	negative_list = [0, 1]
	for i in range(n-1):
		negative_list.append(negative_list[-2]-negative_list[-1])
	return negative_list

print(negative_fiv(n)[::-1] + positive_fib(n)[1:])
