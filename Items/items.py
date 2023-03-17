# CMPE2850 - Programming Languages
# ICA -
# by jleckie1
# File created: 3/16/2023

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
        print(items)
    except FileNotFoundError as er:
        print(f'Unable to open items file: {er}')


class Item:
    def __init__(self, name, cat, stat, boost):
        self.name = name
        self.category = cat
        self.stat = stat
        self.boost = boost


if __name__ == '__main__':
    init()
