# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on 3/16/2023
"""

import random
items = list()


def init():
    try:
        f = open('Items.csv', 'rt')
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


def check_items():
    for x in items:
        print(vars(x))
        for y in [a for a in dir(x) if a[:2] != '__']:
            print(y, end=', ')
        print('\b\b')


class Item:
    def __init__(self, name, cat, stat, boost):
        self.name = name
        self.category = cat
        self.stat = stat
        self.boost = boost


if __name__ == '__main__':
    init()
    check_items()
