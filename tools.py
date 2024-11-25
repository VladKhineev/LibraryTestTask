import os

def clear_console():
    os.system('cls')

def message_output(message):
    clear_console()
    input(message)
    clear_console()

def line():
    print(30 * '*')

def func_with_clear_console(func, stop_clear = False):
    if stop_clear:
        clear_console()
        func()
        input()
        clear_console()
    else:
        clear_console()
        func()
        clear_console()