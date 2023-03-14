# CMPE2850 - Programming Languages
# ICA0 - Name
# by Joel Leckie
# File created: 2023-03-14

import characters

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
    f = open("player.txt", "wt")
    temp = f.read()
    if temp.contains("Name: " + p.name):

