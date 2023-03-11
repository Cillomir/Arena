# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:17:52 2023
"""

import characters
import area
import menu

width = height = 10

walls = [(2, 2), (2, height - 3), (width - 3, 2), (width - 3, height - 3)]
for x in range(width):
    for y in range(height):
        if x == 0 or y == 0 or x == width - 1 or y == height - 1:
            walls.append((x, y))

all_creatures = list()

place = area.Area(width, height, walls)
person = characters.PC('User', width//2, height//2)
all_creatures.append(person)
all_creatures.append(characters.Mob(3, 3))
all_creatures.append(characters.Mob(4, 3))


def __main__():
    while True:
        place.show(all_creatures)
        menu.menu(person, place)
        for c in all_creatures:
            if type(c) is characters.Mob:
                c.move(place.exits(c.loc_x, c.loc_y))


__main__()
