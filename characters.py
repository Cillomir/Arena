# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:22:10 2023
"""


import random
import Items.items as it
it.init('Items/Items.csv')


class Character:
    def __init__(self, name: str, loc_x: int, loc_y: int, health: int, stamina: int, mana: int,
                 strength: int, agility: int, intellect: int, wisdom: int, fortitude: int,
                 defense: dict[str, int], resist: dict[str, int]):
        self.name = name
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.dead = False
        self.in_combat = False
        self.inventory = list()
        self.health = {'current': health, 'max': health}
        self.stamina = {'current': stamina, 'max': stamina}
        self.mana = {'current': mana, 'max': mana}
        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.wisdom = wisdom
        self.fortitude = fortitude
        self.defense = {'armor': 0 if 'armor' not in defense else defense['armor'],
                        'reflex': 0 if 'reflex' not in defense else defense['reflex'],
                        'cut': 0 if 'cut' not in defense else defense['cut'],
                        'stab': 0 if 'stab' not in defense else defense['stab'],
                        'bash': 0 if 'bash' not in defense else defense['bash']}
        self.resist = {'fire': 0 if 'fire' not in resist else resist['fire'],
                       'water': 0 if 'water' not in resist else resist['water'],
                       'earth': 0 if 'earth' not in resist else resist['earth'],
                       'air': 0 if 'air' not in resist else resist['air'],
                       'cold': 0 if 'cold' not in resist else resist['cold'],
                       'electric': 0 if 'electric' not in resist else resist['electric'],
                       'toxin': 0 if 'toxin' not in resist else resist['toxin'],
                       'poison': 0 if 'poison' not in resist else resist['poison'],
                       'light': 0 if 'light' not in resist else resist['light'],
                       'dark': 0 if 'dark' not in resist else resist['dark'],
                       'disease': 0 if 'disease' not in resist else resist['disease']}


class Mob(Character):
    def __init__(self, name, loc_x: int, loc_y: int, health: int, stamina: int, mana: int,
                 strength: int, agility: int, intellect: int, wisdom: int, fortitude: int,
                 defense: dict[str: int], resist: dict[str: int],
                 mob_race, mob_class, mob_job):
        super().__init__(name, loc_x, loc_y, health, stamina, mana,
                         strength, agility, intellect, wisdom, fortitude, defense, resist)
        self.mob_race = mob_race
        self.mob_class = mob_class
        self.mob_job = mob_job

    def move(self, exits: list[str]):
        direction = random.choice(exits)
        if direction == 'n':
            self.loc_y -= 1
        elif direction == 's':
            self.loc_y += 1
        elif direction == 'w':
            self.loc_x -= 1
        elif direction == 'e':
            self.loc_x += 1

    def attack(self, pc_player: 'PC'):
        to_hit = random.randint(1, 20) + self.agility
        if to_hit >= (pc_player.agility + 10):
            damage = random.randint(1, 6) + self.strength
            print(f'\t{self.name} hits you for {damage} damage!')
            pc_player.health['current'] -= damage
            if pc_player.health['current'] <= 0:
                print(f'\tYou have been slain by {self.name}')
                exit()
        else:
            print(f'\t{self.name} tries to attack you but misses')
        return


class NPC(Character):
    def __init__(self, name, loc_x: int, loc_y: int, health: int, stamina: int, mana: int,
                 strength: int, agility: int, intellect: int, wisdom: int, fortitude: int,
                 defense: dict[str: int], resist: dict[str: int],
                 npc_race, npc_class, npc_job):
        super().__init__(name, loc_x, loc_y, health, stamina, mana,
                         strength, agility, intellect, wisdom, fortitude, defense, resist)
        self.npc_race = npc_race
        self.npc_class = npc_class
        self.npc_job = npc_job


class Fighter(Mob):
    def __init__(self, loc_x: 'int', loc_y: 'int', name='Fighter'):
        health, stamina, mana = random.randint(15, 20), random.randint(10, 12), 0
        strength, agility, intellect, wisdom, fortitude = 120, 110, 90, 100, 110
        defense = {'armor': 12, 'reflex': 8, 'cut': 3, 'stab': 2, 'bash': 2}
        resist = {'fire': 0, 'water': 0, 'earth': 0, 'air': 0, 'cold': 0, 'electric': 0,
                  'toxin': 0, 'poison': 0, 'light': 5, 'dark': 5, 'disease': 10}
        mob_race, mob_class, mob_job = 'Human', 'Fighter', 'Arena Gladiator'
        super().__init__(name, loc_x, loc_y, health, stamina, mana,
                         strength, agility, intellect, wisdom, fortitude,
                         defense, resist, mob_race, mob_class, mob_job)
        self.copper = random.randint(2, 12) + random.randint(3, 10)
        self.silver = random.randint(0, 5) + random.randint(1, 5)
        self.gold = random.randint(0, 3) + random.randint(0, 2) + random.randint(0, 2)
        self.inventory.append(it.Weapon('Iron Longsword', 2))
        self.inventory.append(it.Armor('Leather Armor', 1))
        self.inventory.append(it.CoinPouch('Coin Purse', 8))


class Berserker(Mob):
    def __init__(self, loc_x: 'int', loc_y: 'int', name='Berserker'):
        health, stamina, mana = random.randint(18, 24), random.randint(10, 12), 0
        strength, agility, intellect, wisdom, fortitude = 125, 110, 90, 90, 120
        defense = {'armor': 6, 'reflex': 6, 'cut': 4, 'stab': 3, 'bash': 4}
        resist = {'fire': 0, 'water': 0, 'earth': 5, 'air': 0, 'cold': 0, 'electric': 0,
                  'toxin': 0, 'poison': 0, 'light': 0, 'dark': 0, 'disease': 10}
        mob_race, mob_class, mob_job = 'Human', 'Berserker', 'Arena Gladiator'
        super().__init__(name, loc_x, loc_y, health, stamina, mana,
                         strength, agility, intellect, wisdom, fortitude,
                         defense, resist, mob_race, mob_class, mob_job)
        self.copper = random.randint(2, 12) + random.randint(3, 10)
        self.silver = random.randint(0, 5) + random.randint(1, 5)
        self.gold = random.randint(0, 3) + random.randint(0, 2) + random.randint(0, 2)
        self.inventory.append(it.Weapon('Iron Broadsword', 3))
        self.inventory.append(it.Armor('Leather Vest', 1))
        self.inventory.append(it.CoinPouch('Coin Purse', 8))


class Archer(Mob):
    def __init__(self, loc_x: 'int', loc_y: 'int', name='Archer'):
        health, stamina, mana = random.randint(14, 18), random.randint(8, 10), 0
        strength, agility, intellect, wisdom, fortitude = 100, 120, 100, 110, 100
        defense = {'armor': 8, 'reflex': 12, 'cut': 1, 'stab': 4, 'bash': 2}
        resist = {'fire': 0, 'water': 0, 'earth': 0, 'air': 0, 'cold': 5, 'electric': 0,
                  'toxin': 0, 'poison': 5, 'light': 0, 'dark': 0, 'disease': 5}
        mob_race, mob_class, mob_job = 'Human', 'Archer', 'Arena Gladiator'
        super().__init__(name, loc_x, loc_y, health, stamina, mana,
                         strength, agility, intellect, wisdom, fortitude,
                         defense, resist, mob_race, mob_class, mob_job)
        self.copper = random.randint(2, 12) + random.randint(3, 10)
        self.silver = random.randint(0, 5) + random.randint(1, 5)
        self.gold = random.randint(0, 3) + random.randint(0, 2) + random.randint(0, 2)
        self.inventory.append(it.Weapon('Shortbow', 2))
        self.inventory.append(it.Armor('Leather Gambeson', 1))
        self.inventory.append(it.CoinPouch('Coin Purse', 8))


class Rogue(Mob):
    def __init__(self, loc_x: int, loc_y: int, name='Rogue'):
        health, stamina, mana = random.randint(14, 18), random.randint(8, 10), 0
        strength, agility, intellect, wisdom, fortitude = 90, 120, 100, 110, 110
        defense = {'armor': 10, 'reflex': 12, 'cut': 2, 'stab': 3, 'bash': 1}
        resist = {'fire': 0, 'water': 0, 'earth': 0, 'air': 0, 'cold': 0, 'electric': 0,
                  'toxin': 10, 'poison': 5, 'light': 0, 'dark': 0, 'disease': 0}
        mob_race, mob_class, mob_job = 'Human', 'Rogue', 'Arena Gladiator'
        super().__init__(name, loc_x, loc_y, health, stamina, mana,
                         strength, agility, intellect, wisdom, fortitude,
                         defense, resist, mob_race, mob_class, mob_job)
        self.copper = random.randint(2, 12) + random.randint(3, 10)
        self.silver = random.randint(0, 5) + random.randint(1, 5)
        self.gold = random.randint(0, 3) + random.randint(0, 2) + random.randint(0, 2)
        self.inventory.append(it.Weapon('Iron Dagger', 1))
        self.inventory.append(it.Armor('Leather Gambeson', 1))
        self.inventory.append(it.CoinPouch('Coin Purse', 8))


class Merchant(NPC):
    def __init__(self, loc_x: int, loc_y: int, name='Merchant'):
        health, stamina, mana = random.randint(12, 15), random.randint(5, 8), 0
        strength, agility, intellect, wisdom, fortitude = 90, 100, 120, 110, 100
        defense = {'armor': 2, 'reflex': 6, 'cut': 1, 'stab': 1, 'bash': 1}
        resist = {'fire': 0, 'water': 0, 'earth': 0, 'air': 0, 'cold': 0, 'electric': 5,
                  'toxin': 0, 'poison': 5, 'light': 5, 'dark': 5, 'disease': 0}
        npc_race, npc_class, npc_job = 'Human', 'Merchant', 'Arena Merchant'
        super().__init__(name, loc_x, loc_y, health, stamina, mana,
                         strength, agility, intellect, wisdom, fortitude,
                         defense, resist, npc_race, npc_class, npc_job)
        self.copper = random.randint(5, 15) + random.randint(5, 12)
        self.silver = random.randint(3, 8) + random.randint(2, 6)
        self.gold = random.randint(2, 4) + random.randint(1, 4) + random.randint(1, 3)
        self.inventory.append(it.Weapon('Iron Dagger', 1))
        self.inventory.append(it.Armor('Merchant Robes', 1))
        self.inventory.append(it.CoinPouch('Coin Purse', 8))
