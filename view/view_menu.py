from view.view_helper import *
from model.student import Student
def show_main_menu():
    print("1. Add student")
    print("2. Update student")
    print("3. Delete student")
    print("4. Search student (ID)")
    print("5. Exit")

def get_choice_from_menu():
    show_main_menu()
    return get_integer_input("Please choose the menu index: ") 

def process_menu():
    menu_choice = get_choice_from_menu()
    if not menu_choice or menu_choice <= 0 or menu_choice >= 6:
        input("Please input right number. Enter to continue ")
        return
    match menu_choice:
        case 1:
            show_menu_add_student()
        case 2:
            show_update_student()
        case 3:
            show_update_student()
        case 4:
            show_find_student()
        case 5:
            exit()


def show_menu_add_student():
    id = get_string_input("Id:")
    name = get_string_input("Name:")
    address = get_string_input("Adress")
    score = get_float_input("Score")
    return Student(id,name,address,score) 

def show_update_student():
    id = get_string_input("Id:")
    # TODO
    # Find ID here
    #
    name = get_string_input("Name:")
    address = get_string_input("Adress")
    score = get_float_input("Score")
    return Student(id,name,address,score) 

def show_delele_student():
    id = get_string_input("Id:")
    # TODO
    # Find ID here
    #
    return None 

def show_find_student():
    id = get_string_input("Id:")
    # TODO
    # Find ID here
    #
    return None 