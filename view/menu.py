from os import system,name
menu_choice = {

}
def show_main_menu():
    print("1. Add student")
    print("2. Update student")
    print("3. Delete student")
    print("4. Search student (ID)")

def get_choice_from_menu():
    show_main_menu()
    choice = 0
    try:
        choice = int(input("Input your choice: "))
    except:
        # if it not integer => it wrong
        pass
    return choice


def clear_screen():
    # for windows
    if name == 'nt':
        system('cls')
    else:
        system('clear')