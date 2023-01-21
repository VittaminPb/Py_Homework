# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

import re

input_str = input("Введите строку элементов для сжатия: ")

def compress(i_s):
    str_code = ""
    prev_sym = ""
    count = 1
    for sym in i_s:
        if sym != prev_sym:
            if prev_sym:
                str_code += str(count) + prev_sym
            count = 1
            prev_sym = sym
        else:
            count += 1
    else:
        str_code += str(count) + prev_sym
    return str_code

str_code = compress(input_str)
print(f"Входные данные: {input_str }, выходные данные: {str_code}")

