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
        cmd = (input(colors.Effect.reset, 'Your command? ')).lower()
        if cmd == 'n':
            pass
        elif cmd == 'l':
            pass
        elif cmd == 'i':
            pass
        elif cmd == 's':
            pass
        elif cmd == 'q':
            exit()


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
