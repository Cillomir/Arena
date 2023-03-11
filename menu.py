# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:50:00 2023
"""


import area
import characters


def menu(user: 'characters.PC', place: 'area.Area'):
    exits = place.exits(user.loc_x, user.loc_y)
    print('\nAvailable exits (', end='')
    for e in exits:
        print(f"'{e}'", end=',')
    print('\b)')
    print("Other commands: 'q' - Quit")
    cmd = input('Enter a command: ')
    if cmd in exits:
        user.move(cmd)
    elif cmd == 'q':
        exit()
