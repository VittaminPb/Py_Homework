import Modul
import View



def start():
    choice = View.get_choice()
    if choice == 1:
        Modul.check()
    elif choice == 2:
        Modul.sort()
    else:
        print("Некорректный запрос")
    # else:
    #     sorting()


# def check():
#     valid = exists("Phonebook.csv")
#     if not valid:
#         Modul.creating()
# # Modul.writing()
