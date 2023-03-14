# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:50:00 2023
"""


import area
import characters
from os import system
import colors


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~ Pre-Game Menu                          ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def start_menu():
    while True:
        system('cls')
        print(colors.Fore.cyan, colors.Effect.bold, 'Welcome to the Arena', colors.Effect.reset)
        print('\t\tby Joel Leckie\n')
        print(colors.Fore.green, 'Select an option:')
        print('\t[N] - New Game')
        print('\t[L] - Load Game')
        print('\t[I] - Instructions')
        print('\t[S] - Settings')
        print('\t[Q] - Quit')
        print(colors.Effect.reset, end='')
        cmd = (input('Your command? ')).lower()
        if cmd == 'n':
            if new_game():
                break
        elif cmd == 'l':
            pass
        elif cmd == 'i':
            pass
        elif cmd == 's':
            pass
        elif cmd == 'q':
            exit()


def new_game() -> bool:
    print('\n\tType RETURN to go back to the main menu')
    while True:
        name = input('Enter your name, adventurer: ')
        if name == 'RETURN':
            return False
        elif name.isdigit() or not name.isalpha():
            print('Please enter a valid name (a single word containing only letters)')
        else:
            print(f'Welcome {name}')
            break
    return True


def load_game():
    pass


def instructions():
    pass


def settings():
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~ In-Game Menu                           ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menu(user: 'characters.PC', place: 'area.Area'):
    exits = place.exits(user.loc_x, user.loc_y)
    print('\n\tAvailable exits (', end='')
    for e in exits:
        print(f"'{e}'", end=',')
    print('\b)')
    print("\tOther commands: 'q' - Quit")
    cmd = input('\tEnter a command: ')
    if cmd in exits:
        user.move(cmd)
    elif cmd == 'q':
        exit()


if __name__ == '__main__':
    start_menu()
