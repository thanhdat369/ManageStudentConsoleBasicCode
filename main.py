from view.view_menu import *
from view.view_helper import clear_screen
from model.student_manager import StudentLinkedList

student_manager = StudentLinkedList() 

# Test
student1 = Student("1","QA","Di An",10.0)
student2 = Student("SE1","Engineer","Quan 9",6.0)
student3 = Student("SA1","Nothjing","ABC",7.0)
student4 = Student("SD","QA","Go Vap",8.0)
student_manager.insert_new_student(student1)
student_manager.insert_new_student(student2)
student_manager.insert_new_student(student3)
student_manager.insert_new_student(student4)
#
def main():
    while True:
        clear_screen()
        process_menu(student_manager)


try:
    main()
except KeyboardInterrupt:
    # Allow Ctrl C to exit
    exit()


