# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on  2023-03-14
"""


import colors
from characters import Character
from Items.items import Item, Weapon, Armor, OffHand, Wearable, Container, CoinPouch
from json import loads, dumps
from os import system


# Class Skills
# Rage, Bloodthirst, Herald Death, Snipe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~ Create new player data                ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PC(Character):
    def __init__(self, name: 'str', loc_x: 'int', loc_y: 'int'):
        super().__init__(name, loc_x, loc_y, 20)
        # Primary Stats: 80 base, 100 average, 250 normal max, 400 hero max
        self.strength = 80
        self.agility = 80
        self.intellect = 80
        self.wisdom = 80
        self.fortitude = 80
        self.xp = {'level': 1, 'experience': 0, 'training': 5, 'practice': 5, 'skill': 5, 'spell': 5}
        # Secondary Stats
        self.health = {'current': 20, 'max': 20, 'potential': 20}
        self.stamina = {'current': 10, 'max': 10, 'potential': 10}
        self.spirit = {'current': 10, 'max': 10, 'potential': 10}
        self.defense = {'armor': 10, 'avoid': 0, 'cut': 0, 'stab': 0, 'bash': 0}
        self.resist = {'fire': 0, 'water': 0, 'earth': 0, 'air': 0, 'cold': 0, 'electric': 0}
        self.resist += {'toxin': 0, 'poison': 0, 'light': 0, 'dark': 0, 'disease': 0}
        # Other Stats (?): Reputation, Luck, Charm/Poise, Knowledge, Personality
        # Other Stats (?): Sanity, Courage, Constitution, Balance, Vitality
        self.pc_class = None
        self.pc_abilities = None
        # Weapon & Armor Skills:
        self.skill_weapon = {'dagger': 5, 'sword': 0, 'axe': 0, 'hammer': 0, 'staff': 5}
        self.skill_weapon += {'spear': 0, 'polearm': 0, 'lance': 0, 'whip': 0, 'flail': 0}
        self.skill_weapon += {'dart': 0, 'thrown': 0, 'bow': 0, 'crossbow': 0}
        self.skill_weapon += {'stave': 0, 'wand': 0, 'scroll': 0, 'magic items': 0}
        self.skill_exotic = {'hook': 0, 'scythe': 0, 'sickle': 0}
        self.skill_armor = {'shield': 0, 'light': 0, 'medium': 0, 'heavy': 0}
        # Combat Skills:
        self.skills_attacks = {'second': 0, 'third': 0, 'fourth': 0, 'fifth': 0}
        self.skills_combat = {'hand-to-hand': 0, 'blind-fighting': 0, 'martial-arts': 0, 'enhance damage': 0}
        self.skills_combat += {'kick': 0, 'bash': 0, 'sweep': 0, 'charge': 0}
        # Defense Skills:
        self.skill_defense = {'parry': 0, 'dodge': 5, 'block': 0}
        self.skill_defense += {'second defence': 0}
        # Technical Skills:
        self.skill_technical = {'stealth': 0, 'sneak':0, 'hide': 0, 'scan': 0, 'meditation': 0}
        self.skill_technical += {'acrobatics': 0, 'athletics': 0}
        self.skill_technical += {'herbalism': 0, 'scribe': 0}
        self.skill_passive = {'fast healing': 0, 'perception': 0, 'riding': 0}
        self.skill_passive += {'knowledge': 0, 'lore': 0}
        # Mystic Spells:
        self.spell_mystic = {'lay on hands': 0}
        # Abjuration Spells
        # Counterspell 	Cure Disease 	Cure Poison 	Protection From Evil
        # Remove Curse 	Sanctify 	Sanctuary 	Searing Touch
        # Spell Shield
        # Alteration Spells
        # Calm 	Cure Blindness 	Cure Critical 	Cure Light
        # Erase 	Refresh 	Resurrect
        # Enchantment Spells
        # Consecrate Armor 	Consecrate Food 	Consecrate Weapon
        # Illusion Spells
        # Light
        # Invocation Spells
        # Bless
        # Divination Spells
        # Detect Alignment
        # Conjuration Spells
        # Aegis 	Armor 	Create Food 	Create Spring
        # Create Water
        # Abjuration
        # Abjure 	Counterspell 	Dispel Area 	Dispel Magic
        # Room Shield 	Silence
        # Alteration
        # Change Sex 	Death Grip 	Erase 	Flame Wind
        # Haste 	Infravision 	Lava Walk 	Magic Lock
        # Magic Unlock 	Pass Door 	Poison 	Shocking Grasp
        # Spark 	Stone Skin 	Thunderclap 	Underwater Breathing
        # Unnatural Strength 	Weaken
        # Summoning
        # Blink 	Control Winds 	Ice Storm 	Summon Elemental
        # Teleport 	Thunderstorm
        # Enchantment
        # Beacon 	Charm 	Curse 	Levitation
        # Overpressurize 	Recharge Item 	Sleep
        # Illusion
        # Blindness 	Color Spray 	Invisibility 	Light
        # Momentary Darkness
        # Evocation
        # Shield
        # Divination
        # Detect Illusion 	Detect Invisibility 	Detect Magic 	Identify
        # Sense Life 	Wizard Eye
        # Necromancy
        # Animate Dead 	Energy Drain 	Enervation 	Kill
        # Plague 	Slow
        # Conjuration
        # Acid Blast 	Armor 	Circle Of Fire 	Concentration
        # Fireball 	Frost 	Hands Of Wind 	Ice Wind
        # Iceball 	Lightning Bolt 	Magic Bomb 	Magic Dart
        # Magic Message 	Web
        # Chaos
        # Gate Travel 	Nexus 	Plane Travel 	Slow Magic
        # Abjuration
        # Abjure 	Counterspell 	Cure Disease 	Cure Poison
        # Dispel Magic 	Protection From Evil 	Protection From Good 	Remove Curse
        # Sanctuary 	Silence 	Spell Shield 	Tremor
        # Alteration
        # Calm 	Change Sex 	Cure Blindness 	Cure Light
        # Cure Serious 	Erase 	Poison 	Resurrect
        # Spark
        # Summoning
        # Blink 	Combat Blink
        # Enchantment
        # Curse 	Faerie Fire 	Mental Clarity 	Multiply Magic
        # Recharge Item
        # Illusion
        # Blindness 	Light
        # Invocation
        # Bless
        # Divination
        # Detect Alignment 	Detect Illusion 	Detect Invisibility 	Detect Magic
        # Identify 	Remote Sensing 	Sense Life
        # Necromancy
        # Animate Dead 	Cause Light 	Cause Serious 	Plague
        # Slow
        # Conjuration
        # Armor 	Hands Of Wind 	Phalanx
        # Chaos
        # Slow Magic


        self.inventory = list()
        self.equipment = dict()
        self.equipment['Weapon'] = Weapon('Training Sword', 0)
        self.equipment['Off-Hand'] = None
        self.equipment['Armor'] = Armor('Padded Gambeson', 0)
        self.equipment['Head'] = None
        self.equipment['Hands'] = None
        self.equipment['Feet'] = Wearable('Leather Shoes', 'Feet', 'DEX', 0)
        self.inventory.append(Container('Leather Pouch', 8, 'Shoulder'))
        self.inventory.append(CoinPouch('Coin Purse', 8))
        self.inventory[-1].copper = 10
        self.inventory[-1].silver = 5

    def load(self, player_data: 'dict'):
        for key in player_data:
            setattr(self, key, player_data[key])

    def move(self, direction: 'chr'):
        if direction == 'n':
            self.loc_y -= 1
        elif direction == 's':
            self.loc_y += 1
        elif direction == 'w':
            self.loc_x -= 1
        elif direction == 'e':
            self.loc_x += 1

    def see_stats(self):
        system('cls')
        print(f'\nName: {self.name} {" " * (20 - len(self.name))} Location: ({self.loc_x}, {self.loc_y})')
        print(f'\nHealth: {self.health}')
        print(f'\nStrength: {self.str}')
        print(f'Dexterity: {self.dex}')
        print(f'\nWeapon:    ', end='')
        print('Nothing' if self.equipment["Weapon"] is None else self.equipment["Weapon"].name)
        print(f'Off-Hand:  ', end='')
        print('Nothing' if self.equipment["Off-Hand"] is None else self.equipment["Off-Hand"].name)
        print(f'Armor:     ', end='')
        print('Nothing' if self.equipment["Armor"] is None else self.equipment["Armor"].name)
        print(f'Head:      ', end='')
        print('Nothing' if self.equipment["Head"] is None else self.equipment["Head"].name)
        print(f'Hands:     ', end='')
        print('Nothing' if self.equipment["Hands"] is None else self.equipment["Hands"].name)
        print(f'Feet:      ', end='')
        print('Nothing' if self.equipment["Feet"] is None else self.equipment["Feet"].name)
        input("\nPress ENTER to continue...")

    def see_inventory(self):
        print()
        for x in self.inventory:
            print(x.name)
        input("\nPress ENTER to continue...")

    def look_inside(self, container: Container or CoinPouch):
        if type(container) is CoinPouch:
            print(f'\nIn your {container.name} you have:')
            print(f'{container.gold} gold pieces, {container.silver} silver pieces, {container.copper} copper pieces')
        else:
            if len(container.contents) == 0:
                print(f'Your {container.name} is empty. It can hold {container.size} items.')
            else:
                print(f'In your {container.name} you have:')
                print(colors.Fore.cyan)
                for i in container.contents:
                    print(colors.Fore.cyan, i.name)
                print(colors.Effect.reset)
                print(f'It has {len(container.contents)} of {container.size} items in it.')
        input("\nPress ENTER to continue...")

    def wear_item(self):
        pass


player = PC('user', 0, 0)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~ Create new player data                ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def new_player(name: str):
    global player
    player = PC(name, 5, 5)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~ Load player data                      ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_player(name: str) -> bool:
    global player
    try:
        file = open('player.txt', 'rt')
        try:
            temp = file.read()
            load_data = loads(temp)
            if name not in load_data:
                print('There is no record of that character.')
                file.close()
                return False
            player.load(load_data[name])
            print('Successfully loaded save data')
            file.close()
            return True
        except OSError:
            print('Unable to read save file')
            file.close()
            return False
    except OSError:
        print('Unable to load save data')
        return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~ Save player data                      ~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def save_player():
    global player
    file = None
    save_data = dict()
    try:
        file = open("player.txt", "rt")
        try:
            temp = file.read()
            if len(temp) > 0:
                save_data = loads(temp)
                if player.name in save_data:
                    print('That character file already exists.')
                    cmd = input(f'Do you want to overwrite {player.name}? [Y/N] ').lower()
                    while cmd != 'n' and cmd != 'y':
                        print('Please enter a valid option')
                        cmd = input(f'Do you want to overwrite {player.name}? [Y/N] ').lower()
                    if cmd == 'n':
                        return
        except OSError:
            print('Unable to validate save file')
            file.close()
        except FileNotFoundError:
            print('Unable to find existing file')
    except OSError:
        print('Unable to open save file for reading')
    try:
        file = open('player.txt', 'wt')
        try:
            save_data[player.name] = player.__dict__
            file.write(dumps(save_data))
            print('Save successful')
            file.close()
            return
        except TypeError:
            print('Unable to convert player data to save data')
            file.close()
        except OSError:
            print('Unable to write to save file')
            file.close()
            return
    except OSError:
        print('Unable to find or create save file')
        file.close()
        return
