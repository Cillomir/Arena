# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:50:00 2023
"""


import area
import characters


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
