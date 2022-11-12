from view.view_helper import *
from model.student import Student
from model.student_manager import StudentLinkedList

def show_main_menu():
    print("1. Add student")
    print("2. Update student")
    print("3. Delete student")
    print("4. Search student (ID)")
    print("5. Exit")

def get_choice_from_menu():
    show_main_menu()
    return get_integer_input("Please choose the menu index: ") 

def process_menu(student_manager):
    menu_choice = get_choice_from_menu()
    if not menu_choice or menu_choice <= 0 or menu_choice > 6:
        input("Please input right number. Enter to continue ")
        return
    match menu_choice:
        case 1:
            show_menu_add_student(student_manager)
        case 2:
            show_menu_update_student()
        case 3:
            show_menu_update_student()
        case 4:
            show_menu_find_student()
        case 5:
            # Do sth before exit
            exit()
        case 6:
            show_all_student(student_manager) # for test


def show_menu_add_student(student_manager:StudentLinkedList):
    id = get_string_input("Id:").strip()
    student = student_manager.findStudentById(id)
    if student:
        input("The student was existed. Press Enter to back to menu")
        return 
    name = get_string_input("Name:")
    address = get_string_input("Adress: ")
    score = get_float_input("Score: ")
    student = Student(id,name,address,score) 
    isAddSuccess = student_manager.insert_new_student(student)

    input(f"The student was add {'success' if isAddSuccess else'false'}. Press Enter to back to menu")


def show_menu_update_student():
    id = get_string_input("Id:")
    # TODO
    # Find ID here
    #
    name = get_string_input("Name:")
    address = get_string_input("Adress")
    score = get_float_input("Score")
    return Student(id,name,address,score) 

def show_menu_delele_student():
    id = get_string_input("Id:")
    # TODO
    # Find ID here
    #
    return None 

def show_menu_find_student():
    id = get_string_input("Id:")
    # TODO
    # Find ID here
    #
    return None 

def show_all_student(student_manager:StudentLinkedList):
    student_manager.printLL()
    input("-")
    
