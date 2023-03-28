# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:29:32 2023
"""


import characters
import Items.items
import player
from colors import Fore, Back, Effect


class Area:
    def __init__(self, width: 'int', height: 'int', walls: 'list(tuple(int, int))'):
        self.width = int(width)
        self.height = int(height)
        self.walls = walls
    
    def show(self, creatures: 'list[characters.Character]', pc_player: player.PC):
        character = [(pc_player.loc_x, pc_player.loc_y)]
        mobiles = [(c.loc_x, c.loc_y) for c in creatures if type(c) is characters.Mob]

        for y in range(self.height):
            print('', end='\t')
            for x in range(self.width):
                if (x, y) in character:
                    print(Fore.BLUE, '@', end=f'{Effect.RESET} ')
                elif (x, y) in mobiles:
                    print(Fore.RED, '!', end=f'{Effect.RESET} ')
                elif (x, y) not in self.walls:
                    print(Fore.GREEN, '+', end=f'{Effect.RESET} ')
                else:
                    print(Fore.WHITE + Back.WHITE, '#', Effect.RESET, end='')
            print()
    
    def exits(self, loc_x: 'int', loc_y: 'int'):
        directions = list()
        if (loc_x, loc_y - 1) not in self.walls:
            directions.append('n')
        if (loc_x, loc_y + 1) not in self.walls:
            directions.append('s')
        if (loc_x - 1, loc_y) not in self.walls:
            directions.append('w')
        if (loc_x + 1, loc_y) not in self.walls:
            directions.append('e')
        return directions


def show_creatures(loc_x: 'int', loc_y: 'int', creatures: 'list[characters.Character]'):
    mobs = [m for m in creatures if type(m) is characters.Mob and m.loc_x == loc_x and m.loc_y == loc_y]
    if len(mobs) > 0:
        for m in mobs:
            print('\t', Fore.LIGHT_RED, m.name, Effect.RESET)


def show_objects(self, loc_x: 'int', loc_y: 'int', objects: 'list[Items.items.Item]'):
    objs = [o for o in objects if o.loc_x == loc_x and o.loc_y == loc_y]
    if len(objs) > 0:
        for o in objs:
            print('\t', Fore.YELLOW, o.name, Effect.RESET)
