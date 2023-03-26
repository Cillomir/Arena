# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:17:52 2023
"""

import menu
import characters
import player
import area
import ticker
import colors
import random
from os import system

colors.init()
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
all_creatures.append(characters.Mob('A Fighter', room[0], room[1], 15, 5, 4))
room = random.choice(arena)
all_creatures.append(characters.Mob('A Fighter', room[0], room[1], 15, 5, 4))


def mob_timer_tick():
    for c in all_creatures:
        if type(c) is characters.Mob and random.randint(0, 30 - mob_timer.count % 30) <= 5:
            c.move(place.exits(c.loc_x, c.loc_y))
            mob_timer.count = 0
    if len([c for c in all_creatures if type(c) is characters.Mob]) < 2:
        if mob_timer.mob_count >= 100 and random.randint(0, 120 - mob_timer.mob_count) < 5:
            rooms = [loc for loc in arena if loc != (player.player.loc_x, player.player.loc_y)]
            mob_room = rooms[random.choice(rooms)]
            all_creatures.append(characters.Mob(mob_room[0], mob_room[1]))
            mob_timer.mob_count = 0
        else:
            mob_timer.mob_count += 1


def combat_timer_tick(user: player.PC, mob: characters.Mob):
    combat_timer.count += 1
    user.attack(mob)
    if not mob.dead:
        mob.attack(user)


mob_timer = ticker.Scheduler(1, mob_timer_tick)
mob_timer.mob_count = 0
#combat_timer = ticker.Scheduler(5, combat_timer_tick)
#combat_timer.combat_count = 0


def __main__():
    menu.start_menu()
    all_creatures.append(player.player)
    mob_timer.start()
    while True:
        system('cls')
        print('\n\n\n')
        place.show(all_creatures)
        area.show_creatures(player.player.loc_x, player.player.loc_y, all_creatures)
        if menu.menu(player.player, place):
            print("Quitting...")
            mob_timer.stop()
            exit()


__main__()
