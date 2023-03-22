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
        print('\t', colors.Fore.blue, '[N]', colors.Effect.reset, ' - New Game')
        print('\t', colors.Fore.blue, '[L]', colors.Effect.reset, ' - Load Game')
        print('\t', colors.Fore.blue, '[I]', colors.Effect.reset, ' - Instructions')
        print('\t', colors.Fore.blue, '[S]', colors.Effect.reset, ' - Settings')
        print('\t', colors.Fore.blue, '[Q]', colors.Effect.reset, ' - Quit')
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
            name = name[0].upper() + name[1:].lower()
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
            name = name[0].upper() + name[1:].lower()
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
def menu(user: player.PC, place: area.Area):
    exits = place.exits(user.loc_x, user.loc_y)
    print('\n\tAvailable exits (', end='')
    for e in exits:
        print(f"'{e}'", end=',')
    print('\b)')
    print("\tOther commands: 'stats', 'inventory', 'save', 'quit'")
    cmd = input('\tEnter a command: ')
    cmd = cmd.lower().strip()
    if cmd == 'gold' or cmd == 'silver' or cmd == 'copper' or cmd == 'coin' or cmd == 'money':
        user.look_inside(user.inventory[1])
    elif cmd == 'st' or cmd == 'stat' or cmd == 'stats':
        player.player.see_stats()
    elif cmd == 'in' or cmd == 'inv' or cmd == 'inventory':
        player.player.see_inventory()
    elif cmd == "sav" or cmd == 'save':
        player.save_player()
    elif cmd == 'q' or cmd == 'qu' or cmd == 'quit':
        return True
    else:
        spl = read_input(cmd)
        if spl == (None, None):
            return False
        elif spl[0] == 'look' and spl[1] == 'around':
            return False
        elif spl[0] == 'direction' and spl[1] in exits:
            user.move(spl[1])
        elif spl[0] == 'mob':
            pass
        elif spl[0] == 'container':
            pass
        elif spl[0] == 'attack':
            pass
        elif spl[0] == 'shoot':
            pass
    return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~ Input Interpreter                      ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_input(user_input: 'str') -> (str, str) or (None, None):
    if user_input == 's' or user_input == 'sou' or user_input == 'sout' or user_input == 'south':
        return 'direction', 's'
    elif user_input == 'n' or user_input == 'nor' or user_input == 'nort' or user_input == 'north':
        return 'direction', 'n'
    elif user_input == 'e' or user_input == 'eas' or user_input == 'east':
        return 'direction', 'e'
    elif user_input == 'w' or user_input == 'wes' or user_input == 'west':
        return 'direction', 'w'
    spl = user_input.split(' ')
    if len(spl) <= 1:
        return None, None
    if spl[0] == 'exa' or spl[0] == 'exam' or spl[0] == 'exami' or spl[0] == 'examin' or spl[0] == 'examine':
        return 'mob', spl[1]
    if spl[0] == 'l' or spl[0] == 'loo' or spl[0] == 'look':
        if spl[1] == 'at' and len(spl) > 2:
            return 'mob', spl[2]
        elif spl[1] == 'in' and len(spl) > 2:
            return 'container', spl[2]
        elif spl[1] == 'around' or spl[1] == 'aroun' or spl[1] == 'ar':
            return 'look', 'around'
        else:
            return None, None
    elif spl[0] == 'ki' or spl[0] == 'kil' or spl[0] == 'kill':
        return 'attack', spl[1]
    elif spl[0] == 'hi' or spl[0] == 'hit' or spl[0] == 'sta' or spl[0] == 'stab':
        return 'attack', spl[1]
    elif spl[0] == 'att' or spl[0] == 'atta' or spl[0] == 'attac' or spl[0] == 'attack':
        if spl[1] == 's' or spl[1] == 'sou' or spl[1] == 'sout' or spl[1] == 'south':
            return 'shoot', 's'
        if spl[1] == 'n' or spl[1] == 'nor' or spl[1] == 'nort' or spl[1] == 'north':
            return 'shoot', 'n'
        if spl[1] == 'e' or spl[1] == 'eas' or spl[1] == 'east':
            return 'shoot', 'e'
        if spl[1] == 'w' or spl[1] == 'wes' or spl[1] == 'west':
            return 'shoot', 'w'
        else:
            return 'attack', spl[1]
    if spl[0] == 'sh' or spl[0] == 'sho' or spl[0] == 'shoo' or spl[0] == 'shoot':
        if spl[1] == 's' or spl[1] == 'sou' or spl[1] == 'sout' or spl[1] == 'south':
            return 'shoot', 's'
        if spl[1] == 'n' or spl[1] == 'nor' or spl[1] == 'nort' or spl[1] == 'north':
            return 'shoot', 'n'
        if spl[1] == 'e' or spl[1] == 'eas' or spl[1] == 'east':
            return 'shoot', 'e'
        if spl[1] == 'w' or spl[1] == 'wes' or spl[1] == 'west':
            return 'shoot', 'w'
    if spl[0] == 'fi' or spl[0] == 'fir' or spl[0] == 'fire':
        if spl[1] == 's' or spl[1] == 'sou' or spl[1] == 'sout' or spl[1] == 'south':
            return 'shoot', 's'
        if spl[1] == 'n' or spl[1] == 'nor' or spl[1] == 'nort' or spl[1] == 'north':
            return 'shoot', 'n'
        if spl[1] == 'e' or spl[1] == 'eas' or spl[1] == 'east':
            return 'shoot', 'e'
        if spl[1] == 'w' or spl[1] == 'wes' or spl[1] == 'west':
            return 'shoot', 'w'
    return None, None


if __name__ == '__main__':
    start_menu()
