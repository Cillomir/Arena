# CMPE2850 - Programming Languages
# ICA -
# by jleckie1
# File created: 3/16/2023

import random


def init():
    f = open('Items.csv', 'rt')
    items = list()
    for i in f:
        items.add(i)
    print(items)
