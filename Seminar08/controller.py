import view
from statistics import mean


main_dct = {}
student_name = []
lessons = []


def start():
    while True:
        op = view.get_op()
        if op == 1:
            student = view.input_student()
            if student not in student_name:
                main_dct[student] = {}
                student_name.append(student)
                if lessons:
                    for less in lessons:
                        main_dct[student][less] = []
        elif op == 2:
            less = view.input_lesson()
            lessons.append(less)
            for name in student_name:
                main_dct[name][less] = []
        elif op == 3:
            name, less, mark = view.input_mark()
            main_dct[name][less].append(mark)
        elif op == 4:
            print(main_dct)
        elif op == 5:
            name = view.get_name_to_show()
            print(f"Оценки {name} : {main_dct[name]}")
        elif op == 6:
            name = view.get_name_to_show()
            count = 0
            sum = 0
            for mark in main_dct:
                count += 1
                sum += main_dct[mark]
            mark_avg = sum/count
            print(f"Средняя оценка {name} : {mark_avg}")
        elif op == 7:
            break
        print(main_dct)
