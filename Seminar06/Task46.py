# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degree(num, deg):
    if (deg < 0):
        return "Я так еще не умею ))"
    if (deg == 1):
        return (num)
    if (deg != 1):
        return (num * degree(num, deg - 1))

num = int(input("Введите число: "))
deg = int(input("Введите степень: "))

print(f"A = {num}, B = {deg} ->", degree(num, deg))