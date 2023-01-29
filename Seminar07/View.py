def get_choice():
    cho = int(input("выберите действие: 1 - создание записи, 2 - вывод справочника: "))
    return cho
   

def get_info():
    ph_book = []
    ID = int(input("Введите ID: "))
    ph_book.append(ID)
    last_name = input("Введите фамилию: ")
    ph_book.append(last_name)
    first_name = input("Введите имя: ")
    ph_book.append(first_name)
    phone_number = int(input("Введите номер телефона: "))
    ph_book.append(phone_number)
    comment = input("Введите комментарий: ")
    ph_book.append(comment)
    return ph_book
