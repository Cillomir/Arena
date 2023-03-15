# CMPE2850 - Programming Languages
# ICA0 - Name
# by Joel Leckie
# File created: 2023-03-14

import characters
from json import loads, dumps

player = characters.PC('user', 0, 0)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~ Create new player data                ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def new_player(name: str):
    global player
    player = characters.PC(name, 5, 5)


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
            return
    except OSError:
        print('Unable to open save file for reading')
        file.close()
        return
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

