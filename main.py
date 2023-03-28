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
import Items.items as items
from os import system

items.init()

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
all_creatures.append(characters.Fighter(room[0], room[1], 'A Fighter'))
room = random.choice(arena)
all_creatures.append(characters.Fighter(room[0], room[1], 'A Fighter'))


def mob_timer_tick():
    for c in all_creatures:
        if type(c) is characters.Mob and random.randint(0, 30 - mob_timer.count % 30) <= 5:
            c.move(place.exits(c.loc_x, c.loc_y))
            mob_timer.count = 0
    if len([c for c in all_creatures if type(c) is characters.Mob]) < 2:
        if mob_timer.mob_count >= 100 and random.randint(0, 120 - mob_timer.mob_count) < 5:
            rooms = [loc for loc in arena if loc != (player.player.loc_x, player.player.loc_y)]
            mob_room = rooms[random.choice(rooms)]
            all_creatures.append(characters.Fighter(mob_room[0], mob_room[1]))
            mob_timer.mob_count = 0
        else:
            mob_timer.mob_count += 1


def combat_timer_tick(user: player.PC, mob: characters.Mob):
    #combat_timer.count += 1
    user.attack(mob)
    if not mob.dead:
        mob.attack(user)


def resource_ticker_tick():
    #resource_timer.count += 1
    for r in items.Resource.all_resources:
        if r.node_current < r.node_minimum:
            if r.node_count >= r.node_respawn and random.randint(0, r.node_delay - r.node_count) < 1:
                r.node_current += 1


mob_timer = ticker.Scheduler(1, mob_timer_tick)
#combat_timer = ticker.Scheduler(5, combat_timer_tick)
#resource_timer = ticker.Scheduler(10, resource_timer_tick)


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
