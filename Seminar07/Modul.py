import View
from os.path import exists

def check():
    valid = exists("Phonebook.csv")
    if not valid:
        creating()
    writing()

def creating():
    file = "Phonebook.csv"
    with open(file, "w", encoding="utf-8") as data:
        data.write(f"ID; Фамилия; Имя; Номер телефона; Комментарий\n")

# ph_book = View.get_info()

def writing():
    ph_book = View.get_info()
    file = "Phonebook.csv"
    with open(file, "a", encoding="utf-8") as data:
        data.write(f"{ph_book[0]}; {ph_book[1]}; {ph_book[2]}; {ph_book[3]}; {ph_book[4]}\n")

def sort():
    print("sort")