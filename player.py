# CMPE2850 - Programming Languages
# ICA0 - Name
# by Joel Leckie
# File created: 2023-03-14

import characters
from json import loads, dumps

player = None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~ Create or load player data               ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def new_player(name: str):
    global player
    player = characters.PC(name, 0, 0)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~ Save player                           ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def save_player(p: characters.PC):
    try:
        f = open("player.txt", "wt")
        temp = loads(f.read())
        if temp.has_key(p.name):
            cmd = ''
            print('That character file already exists.')
            cmd = input(f'Do you want to overwrite {p.name}? [Y/N] ').lower()
            while cmd != 'n' and cmd != 'y':
                print('Please enter a valid option')
                cmd = input(f'Do you want to overwrite {p.name}? [Y/N] ').lower()
            if cmd == 'n':
                return
        try:
            temp[p.name] = player
            f.write(temp)
        except OSError:
            print('Unable to write to save file')
            return
    except OSError:
        print('Unable to find or create save file')
        return
    finally:
        f.close()

