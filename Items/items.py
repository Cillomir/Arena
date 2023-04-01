# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on 3/16/2023
"""

import random


def init(path='Items.csv'):
    global all_items, all_resources
    all_items = list()
    all_resources = list()
    try:
        f = open(path, 'rt')
        row = 0
        for i in f:
            if row == 0:
                row += 1
                continue
            item = i.split(",")
            all_items.append(Item(item[0], item[1], item[2], item[3]))
    except FileNotFoundError as er:
        print(f'Unable to open items file: {er}')

    all_resources.append(Resource('Iron Vein', 0, 0, 'Iron', 3, 1, 3, 5))
    all_resources.append(Resource('Steel Vein', 0, 0, 'Steel', 3, 1, 3, 5))
    all_resources.append(Resource('Gold Vein', 0, 0, 'Gold', 3, 1, 3, 5))
    all_resources.append(Resource('Oak Tree', 0, 0, 'Oak', 3, 1, 3, 5))
    all_resources.append(Resource('Maple Tree', 0, 0, 'Maple', 3, 1, 3, 5))
    all_resources.append(Resource('Spruce Tree', 0, 0, 'Spruce', 3, 1, 3, 5))


class Item:
    """ General item category """
    all_items = list()

    def __init__(self, name, category, stat, boost):
        self.name = name
        self.category = category
        self.stat = stat
        self.boost = boost
        self.loc_x = -1
        self.loc_y = -1
        Item.all_items.append(self)


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
    for x in Item.all_items:
        print(vars(x))
        for y in [a for a in dir(x) if a[:2] != '__']:
            print(y, end=', ')
        print('\b\b')


if __name__ == '__main__':
    init()
    check_items()


class Resource:
    all_resources = list()

    def __init__(self, name: str, loc_x: int, loc_y: int,
                 node_type: str, amount: int, minimum: int, respawn: int, delay: int):
        self.name = name
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.node_type = node_type
        if node_type == 'Iron':
            self.resource_type = 'Iron Ore'
        elif node_type == 'Steel':
            self.resource_type = 'Steel Ore'
        elif node_type == 'Gold':
            self.resource_type = 'Gold Ore'
        elif node_type == 'Oak' or node_type == 'Maple' or node_type == 'Spruce':
            self.resource_type = 'Wood Logs'
        self.node_current = amount
        self.node_maximum = amount
        self.node_minimum = minimum
        self.node_count = 0
        self.node_respawn = respawn
        self.node_delay = delay
        Resource.all_resources.append(self)
