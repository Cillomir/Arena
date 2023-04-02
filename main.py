# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:17:52 2023
"""

import menu
import characters
import player
import area
import schedules
import colors
import random
import Items.items as items
from os import system

items.init('Items/Items.csv')
colors.init()

width = height = 10
walls = [(2, 2), (2, height - 3), (width - 3, 2), (width - 3, height - 3)]

for x in range(width):
    for y in range(height):
        if x == 0 or y == 0 or x == width - 1 or y == height - 1:
            walls.append((x, y))


arena = area.Area(width, height, walls)
arena_spawn = list()
for x in range(arena.width):
    for y in range(arena.height):
        if (x, y) not in arena.walls:
            arena_spawn.append((x, y))

room = random.choice(arena_spawn)
characters.Fighter(room[0], room[1], 'A Fighter')
room = random.choice(arena_spawn)
characters.Fighter(room[0], room[1], 'A Fighter')


def __main__():
    menu.start_menu()
    schedules.mob_timer.start()
    while True:
        system('cls')
        print('\n\n\n')
        arena.show(characters.Character.all_characters, player.main_player)
        area.show_creatures(player.main_player.loc_x, player.main_player.loc_y, characters.Character.all_characters)
        if menu.menu(arena):
            print("Quitting...")
            schedules.mob_timer.stop()
            exit()


if __name__ == '__main__':
    __main__()
