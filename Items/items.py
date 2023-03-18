# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on 3/16/2023
"""

import random
items = list()


def init(path='Items.csv'):
    try:
        f = open(path, 'rt')
        global items
        row = 0
        for i in f:
            if row == 0:
                row += 1
                continue
            item = i.split(",")
            items.append(Item(item[0], item[1], item[2], item[3]))
    except FileNotFoundError as er:
        print(f'Unable to open items file: {er}')


class Item:
    """ General item category """
    def __init__(self, name, category, stat, boost):
        self.name = name
        self.category = category
        self.stat = stat
        self.boost = boost
        self.loc_x = -1
        self.loc_y = -1


class Weapon(Item):
    def __init__(self, name, boost):
        Item.__init__(self, name, 'Weapon', 'ATK', boost)


class Armor(Item):
    def __init__(self, name, boost):
        Item.__init__(self, name, 'Armor', 'DEF', boost)


class OffHand(Item):
    def __init__(self, name, boost):
        Item.__init__(self, name, 'Off-Hand', 'DEF', boost)


class Wearable(Item):
    def __init__(self, name, location, stat, boost):
        Item.__init__(self, name, 'Wearable', stat, boost)
        self.location = location


class Container(Item):
    def __init__(self, name, size, kind):
        Item.__init__(self, name, 'Container', None, None)
        self.size = size
        self.kind = kind
        self.contents = list()


class CoinPouch(Container):
    def __init__(self, name, size):
        Container.__init__(self, name, size, 'Money')
        self.gold = 0
        self.silver = 0
        self.copper = 0
        self.total = self.gold + self.silver + self.copper

def check_items():
    """ For testing item information and parsing"""
    for x in items:
        print(vars(x))
        for y in [a for a in dir(x) if a[:2] != '__']:
            print(y, end=', ')
        print('\b\b')


if __name__ == '__main__':
    init()
    check_items()
