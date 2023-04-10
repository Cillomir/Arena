# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:29:32 2023
"""


import random
import characters
import Items.items
import player
from Helpers.colors import Fore, Back, Effect
from Helpers.unicode import Blocks


class Area:
    def __init__(self, width: 'int', height: 'int', walls: 'list(tuple(int, int))'):
        self.width = int(width)
        self.height = int(height)
        self.walls = walls
    
    def show(self, creatures: 'list[characters.Character]', pc_player: player.PC):
        character = [(pc_player.loc_x, pc_player.loc_y)]
        mobiles = [(c.loc_x, c.loc_y) for c in creatures if type(c) is characters.Mob]

        for yi in range(self.height):
            print('', end='\t')
            for xi in range(self.width):
                if (xi, yi) in character:
                    print(Fore.BLUE, '@', end=f'{Effect.RESET} ')
                elif (xi, yi) in mobiles:
                    print(Fore.RED, '!', end=f'{Effect.RESET} ')
                elif (xi, yi) not in self.walls:
                    print(Fore.GREEN, '+', end=f'{Effect.RESET} ')
                else:
                    print(Fore.LIGHT_GREY + Back.WHITE, '#', Effect.RESET, end='')
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


def show_objects(loc_x: 'int', loc_y: 'int', objects: 'list[Items.items.Item]'):
    objs = [o for o in objects if o.loc_x == loc_x and o.loc_y == loc_y]
    if len(objs) > 0:
        for o in objs:
            print('\t', Fore.YELLOW, o.name, Effect.RESET)


class Zone:
    def __init__(self, height: int, width: int, border_walls: bool, walls: list[tuple[int, int]] = list(),
                 pillars: list[tuple[int, int]] = list(), buildings: list[tuple[int, int]] = list(),
                 doors_h: list[tuple[int, int]] = list(), doors_v: list[tuple[int, int]] = list(),
                 gates_h: list[tuple[int, int]] = list(), gates_v: list[tuple[int, int]] = list(),
                 trees: list[tuple[int, int]] = list(), bushes: list[tuple[int, int]] = list()):
        self.width = width * 2
        self.height = height
        self.blk = dict()
        for yi in range(self.height):
            for xi in range(self.width):
                self.blk[(xi, yi)] = (Fore.WHITE, Back.BLACK, Blocks.space)

        # BORDER WALLS
        if border_walls:
            for xi in range(self.width):
                self.blk[xi, 0] = (Fore.WHITE, Back.BLACK, Blocks.box_double_hor)
                self.blk[xi, self.height - 1] = (Fore.WHITE, Back.BLACK, Blocks.box_double_hor)
            for yi in range(self.height):
                self.blk[0, yi] = (Fore.WHITE, Back.BLACK, Blocks.box_double_ver)
                self.blk[self.width - 1, yi] = (Fore.WHITE, Back.BLACK, Blocks.box_double_ver)
            self.blk[0, 0] = (Fore.WHITE, Back.BLACK, Blocks.nw_double)
            self.blk[0, self.height - 1] = (Fore.WHITE, Back.BLACK, Blocks.sw_double)
            self.blk[self.width - 1, 0] = (Fore.WHITE, Back.BLACK, Blocks.ne_double)
            self.blk[self.width - 1, self.height - 1] = (Fore.WHITE, Back.BLACK, Blocks.se_double)

        # BUILDINGS
        self.buildings = buildings
        for b in buildings:
            self.blk[b[0] * 2 - 2, b[1] - 0] = (Fore.WHITE, Back.BLACK, Blocks.sw_curve)
            self.blk[b[0] * 2 - 1, b[1] - 0] = (Fore.BLUE, Back.BLACK, Blocks.door_hor)
            self.blk[b[0] * 2 + 0, b[1] - 0] = (Fore.BLUE, Back.BLACK, Blocks.door_hor)
            self.blk[b[0] * 2 + 1, b[1] - 0] = (Fore.BLUE, Back.BLACK, Blocks.door_hor)
            self.blk[b[0] * 2 + 2, b[1] - 0] = (Fore.WHITE, Back.BLACK, Blocks.se_curve)
            self.blk[b[0] * 2 - 2, b[1] - 1] = (Fore.WHITE, Back.BLACK, Blocks.nw_curve)
            self.blk[b[0] * 2 - 1, b[1] - 1] = (Fore.WHITE, Back.BLACK, Blocks.hor_thin)
            self.blk[b[0] * 2 + 0, b[1] - 1] = (Fore.WHITE, Back.BLACK, Blocks.hor_thin)
            self.blk[b[0] * 2 + 1, b[1] - 1] = (Fore.WHITE, Back.BLACK, Blocks.hor_thin)
            self.blk[b[0] * 2 + 2, b[1] - 1] = (Fore.WHITE, Back.BLACK, Blocks.ne_curve)

        # OTHER (Pillars, Trees, Bushes, etc.)
        self.pillars = pillars
        self.trees = trees
        self.bushes = bushes
        for p in pillars:
            self.blk[(p[0] * 2, p[1])] = (Fore.WHITE, Back.BLACK, Blocks.pillar)
        for t in trees:
            self.blk[(t[0] * 2, t[1])] = (Fore.GREEN, Back.BLACK, Blocks.tree)
        for b in bushes:
            self.blk[(b[0] * 2, b[1])] = (Fore.LIGHT_GREEN, Back.BLACK, Blocks.bush)

        self.doors_h = doors_h
        self.doors_v = doors_v
        self.gates_h = gates_h
        self.gates_v = gates_v
        self.spawn = list()
        for xi in range(self.width):
            for yi in range(self.height):
                if (xi, yi) not in walls:
                    self.spawn.append((xi, yi))

    def draw_zone(self):
        reset = Effect.RESET
        for yi in range(self.height):
            print('', end='\t')
            for xi in range(self.width):
                if (xi, yi) in self.blk.keys():
                    print(self.blk[(xi, yi)][0] + self.blk[(xi, yi)][1] + self.blk[(xi, yi)][2], end=f'')
            print(reset)


def zone_arena():
    width = height = 10
    walls = [(2, 2), (2, height - 3), (width - 3, 2), (width - 3, height - 3)]
    zone = Zone(height, width, True, walls)

    room = random.choice(zone.spawn)
    characters.Fighter(room[0], room[1], 'A Fighter')
    room = random.choice(zone.spawn)
    characters.Fighter(room[0], room[1], 'A Fighter')
    return zone


def zone_city():
    width = 25
    height = 20
    buildings = [(3, 3), (6, 3), (9, 3), (15, 3), (18, 3), (21, 3),
                 (3, 6), (6, 6), (9, 6), (15, 6), (18, 6), (21, 6),
                 (3, 9), (6, 9), (9, 9), (15, 9), (18, 9), (21, 9),
                 (3, 14), (6, 14), (9, 14), (15, 14), (18, 14), (21, 14),
                 (3, 17), (6, 17), (9, 17), (15, 17), (18, 17), (21, 17)]
    walls = list()
    for b in buildings:
        walls.extend([(b[0] - 1, b[1] - 1), (b[0], b[1] - 1), (b[0] + 1, b[1] - 1)])
        walls.extend([(b[0] - 1, b[1]), (b[0] + 1, b[1])])
    zone = Zone(height, width, True, walls, buildings=buildings)
    return zone


if __name__ == '__main__':
    city = zone_city()
    city.draw_zone()

