# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:17:52 2023
"""

import characters
import area
import menu
import player
import random
import ticker
from os import system

width = height = 10

walls = [(2, 2), (2, height - 3), (width - 3, 2), (width - 3, height - 3)]
for x in range(width):
    for y in range(height):
        if x == 0 or y == 0 or x == width - 1 or y == height - 1:
            walls.append((x, y))

all_creatures = list()

place = area.Area(width, height, walls)
arena = list()
for x in range(place.width):
    for y in range(place.height):
        if (x, y) not in place.walls:
            arena.append((x, y))
room = random.choice(arena)
all_creatures.append(characters.Mob('Mob', room[0], room[1], 15, 5, 4))
room = random.choice(arena)
all_creatures.append(characters.Mob('Mob', room[0], room[1], 15, 5, 4))


def __main__():
    menu.start_menu()
    all_creatures.append(player.player)
    tick.start()
    while True:
        system('cls')
        print('\n\n\n')
        place.show(all_creatures)
        if menu.menu(player.player, place):
            print("Quitting...")
            tick.stop()
            exit()


def timer_tick():
    for c in all_creatures:
        if type(c) is characters.Mob and random.randint(0, 30 - tick.count % 30) <= 5:
            c.move(place.exits(c.loc_x, c.loc_y))
            tick.count = 0
    if len([c for c in all_creatures if type(c) is characters.Mob]) < 2:
        if tick.mob_count >= 100 and random.randint(0, 120 - tick.mob_count) < 5:
            rooms = [loc for loc in arena if loc != (player.player.loc_x, player.player.loc_y)]
            room = rooms[random.choice(rooms)]
            all_creatures.append(characters.Mob(room[0], room[1]))
            tick.mob_count = 0
        else:
            tick.mob_count += 1


tick = ticker.Scheduler(1, timer_tick)
tick.mob_count = 0

__main__()
