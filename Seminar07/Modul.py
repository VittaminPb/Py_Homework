import View
from os.path import exists
import csv


def check():
    valid = exists("Phonebook.csv")
    if not valid:
        creating()
    writing()


def creating():
    file = "Phonebook.csv"
    with open(file, "w", encoding="utf-8") as data:
        data.write(f"ID; Фамилия; Имя; Номер телефона; Комментарий\n")


def writing():
    ph_book = View.get_info()
    file = "Phonebook.csv"
    with open(file, "a", encoding="utf-8") as data:
        data.write(
            f"{ph_book[0]}; {ph_book[1]}; {ph_book[2]}; {ph_book[3]}; {ph_book[4]}\n")


def read_choice():
    r_choice = View.get_read_choice()
    if r_choice == 1:
        ph_print()
    elif r_choice == 2:
        id_sort()
    elif r_choice == 3:
        name_print()
    else:
        print("Некорректный запрос")


def ph_print():
    file = "Phonebook.csv"
    with open(file, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
        
def id_sort():
    print("здесь будет результат работы функции сортировки тел. справочника")

def name_print():
    print("здесь будет результат работы функции вывода имен и фамилий")
        