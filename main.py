# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:17:52 2023
"""

import characters
import area
import menu
import player
from time import sleep
import random
from threading import Timer
from os import system

width = height = 10

walls = [(2, 2), (2, height - 3), (width - 3, 2), (width - 3, height - 3)]
for x in range(width):
    for y in range(height):
        if x == 0 or y == 0 or x == width - 1 or y == height - 1:
            walls.append((x, y))

all_creatures = list()

place = area.Area(width, height, walls)
all_creatures.append(characters.Mob(3, 3))
all_creatures.append(characters.Mob(4, 3))


def __main__():
    menu.start_menu()
    all_creatures.append(player.player)
    ticker.start()
    global ticker_running
    while True:
        system('cls')
        print('\n\n\n')
        ticker_running = False
        place.show(all_creatures)
        ticker_running = True
        if menu.menu(player.player, place):
            print("Quitting...")
            ticker.cancel()
            exit()
        for c in all_creatures:
            if type(c) is characters.Mob and random.randint(0, tick_count % 20) == 0:
                c.move(place.exits(c.loc_x, c.loc_y))


def tick_event():
    global tick_count
    while True:
        try:
            if ticker_running:
                for c in all_creatures:
                    if type(c) is characters.Mob and random.randint(0, tick_count % 5) == 0:
                        c.move(place.exits(c.loc_x, c.loc_y))
            tick_count += 1
        except:
            print("General error")


ticker = Timer(5, tick_event)
tick_count = 1
ticker_running = True

__main__()
