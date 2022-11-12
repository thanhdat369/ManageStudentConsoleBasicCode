from os import system,name

def clear_screen():
    # for windows
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def get_integer_input(msg):
    int_input = None
    try:
        int_input = int(input(msg).strip())
    except:
        pass
    return int_input

def get_float_input(msg):
    int_input = None
    try:
        int_input = float(input(msg).strip())
    except:
        pass
    return int_input

def get_string_input(msg):
    int_input = None
    try:
        int_input = input(msg).strip()
    except:
        pass
    return int_input
