# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:29:32 2023
"""


import characters
import Items.items
import player
import colors


class Area:
    def __init__(self, width: 'int', height: 'int', walls: 'list(tuple(int, int))'):
        self.width = int(width)
        self.height = int(height)
        self.walls = walls
    
    def show(self, creatures: 'list[characters.Character]'):
        character = [(c.loc_x, c.loc_y) for c in creatures if type(c) is player.PC]
        mobiles = [(c.loc_x, c.loc_y) for c in creatures if type(c) is characters.Mob]

        for y in range(self.height):
            print('', end='\t')
            for x in range(self.width):
                if (x, y) in character:
                    print(colors.Fore.blue, '@', end=f'{colors.Effect.reset} ')
                elif (x, y) in mobiles:
                    print(colors.Fore.red, '!', end=f'{colors.Effect.reset} ')
                elif (x, y) not in self.walls:
                    print(colors.Fore.green, '+', end=f'{colors.Effect.reset} ')
                else:
                    print(colors.Fore.light_grey + colors.Back.light_grey, '#', colors.Effect.reset, end='')
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
            print('\t', colors.Fore.light_red, m.name, colors.Effect.reset)


def show_objects(self, loc_x: 'int', loc_y: 'int', objects: 'list[Items.items.Item]'):
    objs = [o for o in objects if o.loc_x == loc_x and o.loc_y == loc_y]
    if len(objs) > 0:
        for o in objs:
            print('\t', colors.Fore.yellow, o.name, colors.Effect.reset)
