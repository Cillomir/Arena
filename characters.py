# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:22:10 2023
"""


import random


class Character:
    def __init__(self, name: 'str', loc_x, loc_y, health, strength, dexterity):
        self.name = name
        self.health = health
        self.str = strength
        self.dex = dexterity
        self.loc_x = loc_x
        self.loc_y = loc_y


class PC(Character):
    def __init__(self, name: 'str', loc_x: 'int', loc_y: 'int'):
        super().__init__(name, loc_x, loc_y, 20, 6, 5)

    def move(self, direction: 'chr'):
        if direction == 'n':
            self.loc_y -= 1
        elif direction == 's':
            self.loc_y += 1
        elif direction == 'w':
            self.loc_x -= 1
        elif direction == 'e':
            self.loc_x += 1


class Mob(Character):
    def __init__(self, loc_x: 'int', loc_y: 'int'):
        super().__init__('Rando', loc_x, loc_y, 10, 5, 4)

    def move(self, exits: 'list[str]'):
        direction = random.choice(exits)
        if direction == 'n':
            self.loc_y -= 1
        elif direction == 's':
            self.loc_y += 1
        elif direction == 'w':
            self.loc_x -= 1
        elif direction == 'e':
            self.loc_x += 1
