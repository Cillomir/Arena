# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:22:10 2023
"""


import random
import Items.items as it
from player import PC
it.init('Items/Items.csv')


class Character:
    def __init__(self, name: 'str', loc_x, loc_y, health):
        self.name = name
        self.max_health = health
        self.health = health
        self.loc_x = loc_x
        self.loc_y = loc_y


class Mob(Character):
    def __init__(self, name, loc_x: 'int', loc_y: 'int', health, strength, dexterity):
        super().__init__(name, loc_x, loc_y, health)
        self.str = strength
        self.dex = dexterity
        self.inventory = list()
        self.inventory.append(it.items[random.randint(0, len(it.items)-1)])

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

    def attack(self, user: 'PC'):
        to_hit = random.randint(1, 20) + self.dex
        if to_hit >= (user.agility + 10):
            damage = random.randint(1, 6) + self.str
            print(f'\t{self.name} hits you for {damage} damage!')
            user.health['current'] -= damage
            if user.health['current'] <= 0:
                print(f'\tYou have been slain by {self.name}')
                exit()
        else:
            print(f'\t{self.name} tries to attack you but misses')
        return


class Fighter(Mob):
    def __init__(self, loc_x: 'int', loc_y: 'int', name='Fighter'):
        Mob.__init__(self, name, loc_x, loc_y, random.randint(15, 20), 5, 4)
        self.copper = random.randint(2, 12) + random.randint(3, 10)
        self.silver = random.randint(0, 5) + random.randint(1, 5)
        self.gold = random.randint(0, 3) + random.randint(0, 2) + random.randint(0, 2)
        self.inventory = list()
        self.inventory.append(it.Weapon('Iron Longsword', 2))
        self.inventory.append(it.Armor('Leather Gambeson', 1))
        self.inventory.append(it.CoinPouch('Coin Purse', 8))


class Archer(Mob):
    def __init__(self, loc_x: 'int', loc_y: 'int', name='Archer'):
        Character.__init__(self, name, loc_x, loc_y, random.randint(14, 18), 4, 5)
        self.copper = random.randint(2, 12) + random.randint(3, 10)
        self.silver = random.randint(0, 5) + random.randint(1, 5)
        self.gold = random.randint(0, 3) + random.randint(0, 2) + random.randint(0, 2)
        self.inventory = list()
        self.inventory.append(it.Weapon('Shortbow', 2))
        self.inventory.append(it.Armor('Leather Gambeson', 1))
        self.inventory.append(it.CoinPouch('Coin Purse', 8))
