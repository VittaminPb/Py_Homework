import Modul
import View



def start():
    choice = View.get_choice()
    if choice == 1:
        Modul.check()
    elif choice == 2:
        Modul.read_choice()
    else:
        print("Некорректный запрос")

