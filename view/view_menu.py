from view.view_helper import *
from model.student import Student
from model.student_manager import StudentLinkedList

def show_main_menu():
    print("1. Add student")
    print("2. Update student")
    print("3. Delete student")
    print("4. Search student (ID)")
    print("5. Exit")
    print("6. Show all (For Test)")

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
            show_menu_update_student(student_manager)
        case 3:
            show_menu_delele_student(student_manager)
        case 4:
            show_menu_find_student(student_manager)
        case 5:
            # Do sth before exit
            exit()
        case 6:
            show_all_student(student_manager) # for test


def show_menu_add_student(student_manager:StudentLinkedList):
    id = get_string_input("Id:")
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


def show_menu_update_student(student_manager:StudentLinkedList):
    id = get_string_input("Id:")
    student = student_manager.findStudentById(id)
    if not student:
        input("Can not find the student. Press Enter to back to menu")
        return
    
    name = get_string_input("Name:")
    address = get_string_input("Adress")
    score = get_float_input("Score")
    updated_student = Student(id,name,address,score) 

    student.update(updated_student)
    # no need to use student_manager.update because the pointer acess to it
    # student_manager.update_student(updated_student)
    input(f"The student was update success press Enter to back to menu")

def show_menu_delele_student(student_manager:StudentLinkedList):
    id = get_string_input("Id:")
    isDeleteSuccess = student_manager.delete_student(id) 
    input(f"The student was delete \
        {'success' if isDeleteSuccess else 'failed because can not find'}. \
        Press Enter to back to menu")

def show_menu_find_student(student_manager:StudentLinkedList):
    id = get_string_input("Id:")
    student = student_manager.findStudentById(id)
    if not student:
        input("Can not find the student. Press Enter to back to menu")
    print(f"Id: {student.id}")
    print(f"Name: {student.name}")
    print(f"Address: {student.address}")
    print(f"Score: {student.score}")

    input(f"Press Enter to back to Menu")


def show_all_student(student_manager:StudentLinkedList):
    student_manager.printLL()
    input("-")
    
