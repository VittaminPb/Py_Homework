# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. 
# Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. 
# В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 

from random import randint

def input_dat(name):
    x = int(
        input(f"{name}, введите количество конфет (от 1 до 28), которое возьмете: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, некорректный ввод, повторите: "))
    return x


def step_print(name, k, counter, value):
    print(f"{name} сделал свой ход. Он взял {k} конфет, теперь у него {counter}. На столе осталось {value} конфет.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2) 
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        step_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        step_print(player2, k, counter2, value)

if flag:
    print(f"Поздравляем {player1}, он забрал все оставшиеся конфеты и выиграл!")
else:
    print(f"Выиграл {player2}, он забрал все оставшиеся конфеты !")