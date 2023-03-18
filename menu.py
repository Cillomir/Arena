# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:50:00 2023
"""


import area
import characters
from os import system
import colors
import player


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
        if cmd == 'n' or cmd == 'new' or cmd == 'new game':
            if new_game():
                break
        elif cmd == 'l' or cmd == 'load' or cmd == 'load game':
            if load_game():
                break
        elif cmd == 'i' or cmd == 'instruction' or cmd == 'instructions':
            pass
        elif cmd == 's' or cmd == 'setting' or cmd == 'settings':
            pass
        elif cmd == 'q' or cmd == 'quit':
            exit()


def new_game() -> bool:
    print('\n\tType RETURN to go back to the main menu')
    while True:
        name = input('Enter your name, adventurer: ')
        name = name.strip()
        if name == 'RETURN':
            return False
        elif name.isdigit() or not name.isalpha():
            print('Please enter a valid name (a single word containing only letters)')
        else:
            name[0] = name[0].upper()
            print(f'Welcome {name}')
            break
    player.new_player(name)
    return True


def load_game():
    print('\n\tType RETURN to go back to the main menu')
    while True:
        name = input('Enter the name to load: ')
        name = name.strip()
        if name == 'RETURN':
            return False
        elif name.isdigit() or not name.isalpha():
            print('Please enter a valid name (a single word containing only letters)')
        else:
            name[0] = name[0].upper()
            if player.load_player(name):
                print(f'Welcome back {name}')
                break
            else:
                return False
    return True


def instructions():
    pass


def settings():
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~ In-Game Menu                           ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menu(user: 'player.PC', place: 'area.Area'):
    exits = place.exits(user.loc_x, user.loc_y)
    print('\n\tAvailable exits (', end='')
    for e in exits:
        print(f"'{e}'", end=',')
    print('\b)')
    print("\tOther commands: 'stats', 'inventory', 'save', 'quit'")
    cmd = input('\tEnter a command: ')
    cmd = cmd.lower().strip()
    if cmd == 'south' or cmd == 'sout' or cmd == 'sou':
        cmd = 's'
    elif cmd == 'north' or cmd == 'nort' or cmd == 'nor':
        cmd = 'n'
    elif cmd == 'east' or cmd == 'eas':
        cmd = 'e'
    elif cmd == 'west' or cmd == 'wes':
        cmd = 'w'
    if cmd in exits:
        user.move(cmd)
    elif cmd == "sav" or cmd == 'save':
        player.save_player()
    elif cmd == 'st' or cmd == 'stat' or cmd == 'stats':
        player.player.see_stats()
    elif cmd == 'inv' or cmd == 'inventory':
        player.player.see_inventory()
    elif cmd == 'q' or cmd == 'qu' or cmd == 'quit':
        return True
    return False


if __name__ == '__main__':
    start_menu()
