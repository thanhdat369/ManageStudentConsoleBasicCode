from view.view_menu import *
from view.view_helper import clear_screen
from model.student_manager import StudentLinkedList

student_manager = StudentLinkedList() 
def main():
    while True:
        clear_screen()
        process_menu(student_manager)


try:
    main()
except KeyboardInterrupt:
    # Allow Ctrl C to exit
    exit()


