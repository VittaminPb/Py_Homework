def get_op():
    op = int(input("Выберите опцию:\n \
    1 - добавить ученика\n \
    2 - добавить предмет\n \
    3 - выставить оценку\n \
    4 - вывести список учеников\n \
    5 - вывести успеваемость выбранного ученика\n \
    6 - выход\n"))
    return op

def input_student():
    name = input("Введите имя и фамилию >> ")
    return name

def input_lesson():
    less = input("Введите предмет >> ")
    return less

def input_mark():
    name = input("Кому выставляем оценку? >> ")
    less = input("По какому предмету? >> ")
    mark = input("Какую оценку ставим? >> ")
    return name, less, mark

def get_name_to_show():
    name = input("Введите имя для просмотра оценок")
    return name