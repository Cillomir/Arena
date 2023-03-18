# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on  2023-03-14
"""


from characters import Character
from json import loads, dumps
from os import system


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~ Create new player data                ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PC(Character):
    def __init__(self, name: 'str', loc_x: 'int', loc_y: 'int'):
        super().__init__(name, loc_x, loc_y, 20, 6, 5)
        self.inventory = list()

    def load(self, player_data: 'dict'):
        for key in player_data:
            setattr(self, key, player_data[key])

    def move(self, direction: 'chr'):
        if direction == 'n':
            self.loc_y -= 1
        elif direction == 's':
            self.loc_y += 1
        elif direction == 'w':
            self.loc_x -= 1
        elif direction == 'e':
            self.loc_x += 1

    def see_stats(self):
        system('cls')
        print(f'Name: {self.name} {" " * (20 - len(self.name))} Location: ({self.loc_x}, {self.loc_y})')
        print(f'\nHealth: {self.health}')
        print(f'\nStrength: {self.str}')
        print(f'Dexterity: {self.dex}')
        print(f'\nWeapon: {self.weapon}')

    def see_inventory(self):
        for x in self.inventory:
            print(x.name)


player = PC('user', 0, 0)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~ Create new player data                ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def new_player(name: str):
    global player
    player = PC(name, 5, 5)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~ Load player data                      ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_player(name: str) -> bool:
    global player
    try:
        file = open('player.txt', 'rt')
        try:
            temp = file.read()
            load_data = loads(temp)
            if name not in load_data:
                print('There is no record of that character.')
                file.close()
                return False
            player.load(load_data[name])
            print('Successfully loaded save data')
            file.close()
            return True
        except OSError:
            print('Unable to read save file')
            file.close()
            return False
    except OSError:
        print('Unable to load save data')
        return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~ Save player data                      ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def save_player():
    global player
    file = None
    save_data = dict()
    try:
        file = open("player.txt", "rt")
        try:
            temp = file.read()
            if len(temp) > 0:
                save_data = loads(temp)
                if player.name in save_data:
                    print('That character file already exists.')
                    cmd = input(f'Do you want to overwrite {player.name}? [Y/N] ').lower()
                    while cmd != 'n' and cmd != 'y':
                        print('Please enter a valid option')
                        cmd = input(f'Do you want to overwrite {player.name}? [Y/N] ').lower()
                    if cmd == 'n':
                        return
        except OSError:
            print('Unable to validate save file')
            file.close()
        except FileNotFoundError:
            print('Unable to find existing file')
    except OSError:
        print('Unable to open save file for reading')
    try:
        file = open('player.txt', 'wt')
        try:
            save_data[player.name] = player.__dict__
            file.write(dumps(save_data))
            print('Save successful')
            file.close()
            return
        except OSError:
            print('Unable to write to save file')
            file.close()
            return
    except OSError:
        print('Unable to find or create save file')
        file.close()
        return
