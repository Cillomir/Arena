# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:29:32 2023
"""


import random
import characters
import Items.items
import player
from colors import Fore, Back, Effect


class Blocks:
    box_hor_light = hor_thin = hor_wall = u'\u2500'
    box_hor_heavy = hor_thick = hor_fort = u'\u2501'
    box_ver_light = ver_thin = ver_wall = u'\u2502'
    box_ver_heavy = ver_thick = ver_fort = u'\u2503'
    double_dash_hor_light = hor_2dash_thin = window_hor = u'\u254C'
    double_dash_hor_heavy = hor_2dash_thick = window_heavy_hor = u'\u254D'
    double_dash_ver_light = ver_2dash_thin = window_ver = u'\u254E'
    double_dash_ver_heavy = ver_2dash_thick = window_heavy_ver = u'\u254F'
    triple_dash_hor_light = hor_3dash_thin = door_hor = u'\u2504'
    triple_dash_hor_heavy = hor_3dash_thick = door_heavy_hor = u'\u2505'
    triple_dash_ver_light = ver_3dash_thin = door_ver = u'\u2506'
    triple_dash_ver_heavy = ver_3dash_thick = door_heavy_ver = u'\u2507'
    quad_dash_hor_light = hor_4dash_thin = gate_hor = u'\u2508'
    quad_dash_hor_heavy = hor_4dash_thick = gate_heavy_hor = u'\u2509'
    quad_dash_ver_light = ver_4dash_thin = gate_ver = u'\u250A'
    quad_dash_ver_heavy = ver_4dash_thick = gate_heavy_ver = u'\u250B'
    down_right_light = nw_thin = nw_wall = u'\u250C'
    down_right_heavy = nw_thick = nw_fort = u'\u250F'
    down_left_light = ne_thin = ne_wall = u'\u2510'
    down_left_heavy = ne_thick = ne_fort = u'\u2513'
    up_right_light = sw_thin = sw_wall = u'\u2514'
    up_right_heavy = sw_thick = sw_fort = u'\u2517'
    up_left_light = se_thin = se_wall = u'\u2518'
    up_left_heavy = se_thick = se_fort = u'\u251B'
    ver_right_light = west_t_thin = west_t_wall = u'\u251C'
    ver_right_heavy = west_t_thick = west_t_fort = u'\u2523'
    ver_left_light = east_t_thin = east_t_wall = u'\u2524'
    ver_left_heavy = east_t_thick = east_t_fort = u'\u252B'
    hor_down_light = north_t_thin = north_t_wall = u'\u252C'
    hor_down_heavy = north_t_thick = north_t_fort = u'\u2533'
    hor_up_light = south_t_thin = south_t_wall = u'\u2534'
    hor_up_heavy = south_t_thick = south_t_fort = u'\u253B'
    ver_hor_light = cross_thin = center_plus_wall = u'\u253C'
    ver_hor_heavy = cross_thick = center_plus_fort = u'\u254B'
    box_double_hor = hor_double = hor_castle = u'\u2550'
    box_double_ver = ver_double = ver_castle = u'\u2551'
    double_down_right = nw_double = nw_castle = u'\u2554'
    double_down_left = ne_double = ne_castle = u'\u2557'
    double_up_right = sw_double = sw_castle = u'\u255A'
    double_up_left = se_double = se_castle = u'\u255D'
    double_ver_right = west_t_double = west_t_castle = u'\u2560'
    double_ver_left = east_t_double = east_t_castle = u'\u2563'
    double_hor_down = north_t_double = north_t_castle = u'\u2566'
    double_hor_up = south_t_double = south_t_castle = u'\u2569'
    double_ver_hor = cross_double = center_plus_castle = u'\u256C'
    diagonal_cross = u'\u2573'

    nw_curve = u'\u256D'
    ne_curve = u'\u256E'
    se_curve = u'\u256F'
    sw_curve = u'\u2570'
    nw_quadrant = u'\25DC'
    ne_quadrant = u'\25DD'
    se_quadrant = u'\25DE'
    sw_quadrant = u'\25DF'

    space = u'\u0020'
    thin_block = u'\u2591'
    med_block = u'\u2592'
    thick_block = u'\u2593'
    solid_block = u'\u2588'
    angle_box = pillar = u'\u25C8'
    flower = u'\u2698'

    player_m = u'u+1FBC5'
    player_f = u'u+1FBC9'
    npc = mob = u'u+1FBC6'
    tree = u'\u2359'
    bush = u'u+1FBB0'


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
        self.testing = list()
        self.testing.append((4, 5, Blocks.nw_curve))
        self.testing.append((5, 5, Blocks.hor_thin))
        self.testing.append((6, 5, Blocks.ne_curve))
        self.testing.append((4, 4, Blocks.sw_curve))
        self.testing.append((5, 4, Blocks.door_hor))
        self.testing.append((6, 4, Blocks.se_curve))
        self.dict_test = dict()
        self.dict_test[(2, 2)] = Blocks.nw_curve
        self.dict_test[(3, 2)] = Blocks.hor_thin
        self.dict_test[(4, 2)] = Blocks.ne_curve
        self.dict_test[(2, 3)] = Blocks.sw_curve
        self.dict_test[(3, 3)] = Blocks.door_hor
        self.dict_test[(4, 3)] = Blocks.se_curve
        self.width = width
        self.height = height
        for xi in range(self.width):
            self.dict_test[xi, 0] = Blocks.hor_thick
            self.dict_test[xi, height - 1] = Blocks.hor_thick
        for yi in range(self.height):
            self.dict_test[0, yi] = Blocks.ver_thick
            self.dict_test[width - 1, yi] = Blocks.ver_thick
        self.dict_test[0, 0] = Blocks.nw_thick
        self.dict_test[0, self.height - 1] = Blocks.sw_thick
        self.dict_test[self.width - 1, 0] = Blocks.ne_thick
        self.dict_test[self.width - 1, self.height - 1] = Blocks.se_thick
        self.pillars = pillars
        self.doors_h = doors_h
        self.doors_v = doors_v
        self.gates_h = gates_h
        self.gates_v = gates_v
        self.trees = trees
        self.bushes = bushes
        self.buildings = buildings
        self.walls = walls
        if border_walls:
            for xi in range(width):
                for yi in range(height):
                    if xi == 0 or xi == width - 1 or yi == 0 or yi == height - 1:
                        self.walls.append((xi, yi))
        self.spawn = list()
        for xi in range(self.width):
            for yi in range(self.height):
                if (xi, yi) not in self.walls:
                    self.spawn.append((xi, yi))


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
    res = Effect.RESET
    for y in range(city.height):
        print('', end='\t')
        for x in range(city.width):
            if (x, y) in city.doors_h:
                print(Fore.BLUE, Blocks.door_hor, end=f'{res} ')
            elif (x, y) in city.doors_v:
                print(Fore.BLUE, Blocks.door_ver, end=f'{res}')
            elif (x, y) in city.gates_h:
                print(Fore.LIGHT_BLUE, Blocks.gate_hor, end=f'{res}')
            elif (x, y) in city.gates_v:
                print(Fore.LIGHT_BLUE, Blocks.gate_ver, end=f'{res}')
            elif (x, y) in city.pillars:
                print(Fore.DARK_GREY, Blocks.angle_box, end=f'{res}')
            elif (x, y) in city.trees:
                print(Fore.GREEN, Blocks.player_m, end=f'{res}')
            elif (x, y) in city.bushes:
                print(Fore.LIGHT_GREEN, Blocks.player_f, end=f'{res}')
            elif (x, y) in city.dict_test.keys():
                print(Fore.WHITE, city.dict_test[(x, y)], end=f'{res}')
            elif (x, y) not in city.walls:
                print(Fore.GREEN, Blocks.thin_block, end=f'{res}')
            else:
                print(Fore.LIGHT_GREY, Blocks.thick_block, end=f'{res}')
        print()
