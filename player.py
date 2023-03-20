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
# Rage, Bloodthirst, Herald Death, Snipe, Evasion, Vital Strike, Brutal Strike, Cleave
# Backstab, Music, Marksman, Slit Throat, Ambush, Runic Magic, Alchemy, Metallurgy, Impale
# Hamstring, Ice-fist/Fire-fist/Stone-fist/Void-fist

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
        self.defense = {'armor': 10, 'reflex': 0, 'cut': 0, 'stab': 0, 'bash': 0}
        self.resist = {'fire': 0, 'water': 0, 'earth': 0, 'air': 0, 'cold': 0, 'electric': 0}
        self.resist += {'toxin': 0, 'poison': 0, 'light': 0, 'dark': 0, 'disease': 0}
        # Other Stats (?): Reputation, Luck, Charm/Poise, Knowledge, Personality
        # Other Stats (?): Sanity, Courage, Balance
        self.pc_race = None
        self.pc_class = None
        self.pc_job = None
        self.pc_abilities = None
        # Weapon & Armor Skills:
        self.skill_weapon = {'dagger': 5, 'sword': 0, 'axe': 0, 'hammer': 0, 'staff': 5}
        self.skill_weapon += {'two-hand sword': 0, 'two-hand axe': 0, 'two-hand hammer': 0, 'two-hand staff': 0}
        self.skill_weapon += {'spear': 0, 'polearm': 0, 'lance': 0, 'whip': 0, 'flail': 0}
        self.skill_weapon += {'dart': 0, 'javelin': 0, 'thrown': 0, 'sling': 0, 'bow': 0, 'crossbow': 0}
        self.skill_weapon += {'stave': 0, 'wand': 0, 'scroll': 0, 'magic items': 0}
        self.skill_exotic = {'hook': 0, 'scythe': 0, 'sickle': 0, 'bola': 0, 'boomerang': 0}
        self.skill_armor = {'shield': 0, 'light': 0, 'medium': 0, 'heavy': 0}
        # Combat Skills:
        self.skills_attacks = {'second': 0, 'third': 0, 'fourth': 0, 'fifth': 0}
        self.skills_combat = {'hand-to-hand': 0, 'blind-fighting': 0, 'martial-arts': 0, 'enhance damage': 0}
        self.skills_combat += {'kick': 0, 'bash': 0, 'sweep': 0, 'charge': 0, 'grapple': 0, 'feint': 0}
        self.skills_combat += {'defend': 0, 'slash': 0, 'disarm': 0, 'tackle': 0}
        # Defense Skills:
        self.skill_defense = {'parry': 0, 'dodge': 5, 'block': 0}
        self.skill_defense += {'second defence': 0, 'discipline': 0}
        # Technical Skills:
        self.skill_technical = {'stealth': 0, 'sneak': 0, 'hide': 0, 'scan': 0, 'tracking': 0, 'meditation': 0}
        self.skill_technical += {'acrobatics': 0, 'athletics': 0, 'disarm traps': 0, 'snare': 0}
        self.skill_technical += {'herbalism': 0, 'scribe': 0, 'peek': 0, 'thievery': 0, 'forgery': 0, 'lock picking': 0, 'pickpocket': 0}
        self.skill_technical += {'imbue poison': 0}
        self.skill_passive = {'fast healing': 0, 'perception': 0, 'riding': 0, 'detect traps': 0}
        self.skill_passive += {}
        self.skill_passive += {'knowledge': 0, 'lore': 0}
        self.skill_enhancements = {'endurance': 0, 'vitality': 0, 'constitution': 0}

        # Fireshield, Death Grip, Flame Wind, Poison, Shocking Grasp
        # Spark, Thunderclap, Concentration
        # Magic Message, Gate Travel, Nexus, Plane Travel
        # Faerie Fire, Mental Clarity, Multiply Magic, Slow Magic
        # Bar, Cancellation, Describe, Disequilibriate
        # Disrupt Sight, Domination, Esp, Float
        # Force Field, Forget, Geisteblitz, Induce Aggression
        # Irritation, Knock, Memory Drain, Mental Disruption
        # Mesmerize, Mimic, Mind Shield, Nullification Field
        # Pense, Pyrokinesis, Sensory Enhancement, Spook
        # Telesmatic Force, Teleview, Transference, Electrogenic Growth, Fungal Growth
        # Death Grip, Guise Of Nature, Otolithic Growth, Wind Walk
        # Charm, Levitation, Gate Travel, Shadow Door
        # Tinnitus, Circle Of Thorns, Flintstrike, Magic Message
        # Awaken, Condemn, Refresh, Requiem, Excommunicate
        # Augment Aura, Channel Faith, Totem, Shadow Golem, Shadow Imp
        # Beacon, Consecrate Food, Desecrate Armor
        # Elemental Shield, Negation, Pentacle, Swarm
        # Delay Reincarnation, Disjunction, Famine
        # Fatigue, Immobilize, Impede Movement
        # Leech, Leech Conduit, Malediction, Malignancy
        # Shadow Armor, Shadow Light
        # Convocation 	Magic Message


        # Mystic Spells:
        self.spell_mystic = {'lay on hands': 0}
        self.spell_mystic += {'evil eye', 'jinx', 'insanity'}
        # Abjuration Spells: Spells that banish or send away
        self.spell_abjuration = {'cure disease', 'cure poison', 'remove curse'}
        self.spell_abjuration = {'counterspell', 'dispel area', 'dispel magic', 'silence'}
        self.spell_abjuration += {'abjure', 'room shield', 'sanctify', 'sanctuary', 'searing touch'}
        self.spell_protection = {'evil', 'good', 'spell shield'}
        # Alteration Spells: Spells that change an item or persons state
        self.spell_alteration = {'calm', 'cure blindness', 'cure light', 'cure serious', 'cure critical', 'heal'}
        self.spell_alteration += {'haste', 'slow', 'infravision', 'lava walk', 'magic lock', 'magic unlock'}
        self.spell_alteration += {'erase', 'refresh', 'resurrect', 'change sex', 'pass door', 'levitation'}
        self.spell_alteration += {'underwater breathing', 'weaken', 'sleep', 'stoneskin'}
        self.spell_enhance = {'strength', 'unnatural strength', 'agility', 'unnatural agility'}
        self.spell_enhance += {'intellect', 'wisdom', 'fortitude'}
        # Enchantment Spells: Spells that enhance the nature of an item or person
        self.spell_enchantment = {'consecrate armor', 'consecrate weapon', 'consecrate food'}
        self.spell_enchantment += {'beacon', 'charm', 'curse', 'recharge item'}
        # Illusion Spells: Spells that confuse or mislead
        self.spell_illusion = {'light', 'color spray', 'invisibility', 'darkness'}
        self.spell_illusion += {'camouflage', 'concealment'}
        # Invocation Spells: Spells that bring an outside force to bear
        self.spell_invocation = {'bless', 'plague', 'curse', 'bane', 'hex'}
        self.spell_invocation += {'blind', 'deafen', 'confusion'}
        # Divination Spells: Spells that reveal details of an item or person
        self.spell_divination = {'detect alignment', 'detect illusion', 'detect invisible', 'detect magic'}
        self.spell_divination += {'identify', 'sense life', 'wizard eye', 'remote senses', 'infravision', 'read aura'}
        # Conjuration Spells: Spells that mold astral energy into a physical force
        self.spell_conjuration = {'aegis', 'armor', 'create food', 'create water'}
        self.spell_conjuration += {'create spring', 'campfire', 'fountain', 'magic carpet'}
        self.spell_conjuration += {'blink', 'control winds', 'teleport', 'shield', 'hands of wind'}
        self.spell_conjuration += {'whirlwind', 'bubble cluster', 'call lightning'}
        self.spell_summon = {'fire elemental', 'air elemental', 'earth elemental', 'water elemental', 'shade'}
        self.spell_summon += {'find familiar', 'summon familiar', 'summon mount', 'summon', 'word of recall'}
        # Evocation Spells: Spells that cause a physical manifestation of force
        self.spell_evocation = {'ice storm', 'thunderstorm', 'acid blast', 'ice wind', 'tremor'}
        self.spell_evocation += {'circle of fire', 'fireball', 'frost', 'iceball', 'magic missile'}
        self.spell_evocation += {'lightning bolt', 'magic dart', 'spark', 'magic bomb', 'web'}
        # Telekinetic Spells: Spells that can move or manipulate objects from a distance
        self.spell_kinetic = {'telekinesis', 'telekinetic bash', 'telekinetic pierce', 'telekinetic slash'}
        self.spell_kinetic += {'telekinetic wave', 'telekinetic punch', 'telekinetic shield', 'telekinetic explosion'}
        # Necromancy Spells: Spells that effect the life force of a being
        self.spell_necromancy = {'animate dead', 'energy drain', 'enervation', 'kill', 'reanimate', 'life drain'}
        self.spell_necromancy += {'cause light', 'cause serious', 'cause critical', 'harm', 'chill touch'}

        # Evocation
        # Air Evocation, Ash Evocation, Dust Evocation, Earth Evocation
        # Fire Evocation, Ice Evocation, Lightning Evocation, Magma Evocation
        # Minerals Evocation, Ooze Evocation, Radiance Evocation, Salt Evocation
        # Smoke Evocation, Steam Evocation, Vacuum Evocation, Water Evocation
        # Invocation
        # Air Invocation, Ash Invocation, Dust Invocation, Earth Invocation
        # Fire Invocation, Ice Invocation, Lightning Invocation, Magma Invocation
        # Minerals Invocation, Ooze Invocation, Radiance Invocation, Salt Invocation
        # Smoke Invocation, Steam Invocation, Vacuum Invocation, Water Invocation

        # ADVANCED
        # Abjuration
        # Antimagic Sphere
        # Alteration
        # Mutilate, Cure Mutilation, Frenzy, Pustulate, Magnetic Field, Quicksand
        # Summoning
        # Megalith, Monument, Warp
        # Enchantment
        # Bathe, Frostborne, Lava Cloak
        # Illusion
        # Displacement
        # Invocation
        # Air Halo
        # Evocation
        # Chain Lightning, Diseased Cloud, Ice Whip, Landslide
        # Reflective Fireball, Waterspout, Thunderstorm, Ice Storm, Blizzard
        # Divination
        # Illumination
        # Necromancy
        # Necromancers Guile
        # Conjuration
        # Acid Mist, Blood Dance, Cursed Fog, Ember Carom, Lightning Shroud, Poison Gas
        # Soul Sacrifice, Chaos, Air Blast, Buffet, Damnation, Withering Touch


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


def player_race(pc_player: 'PC', pc_race):
    pc_player.pc_race = pc_race
    if pc_race == 'Human':
        pc_player.strength += 10
        pc_player.agility += 10
        pc_player.intellect += 10
        pc_player.wisdom += 10
        pc_player.fortitude += 10
        pass
    elif pc_race == 'Elf':
        pc_player.strength += 5
        pc_player.agility += 20
        pc_player.intellect += 20
        pc_player.wisdom += 20
        pc_player.fortitude += 5
        pass
    elif pc_race == 'Dwarf':
        pc_player.strength += 20
        pc_player.agility += 5
        pc_player.intellect += 10
        pc_player.wisdom += 10
        pc_player.fortitude += 25
        pass
    elif pc_race == 'Halfling':
        pc_player.strength += 5
        pc_player.agility += 20
        pc_player.intellect += 15
        pc_player.wisdom += 20
        pc_player.fortitude += 10
        pass
    elif pc_race == 'Gnome':
        pc_player.strength += 5
        pc_player.agility += 15
        pc_player.intellect += 20
        pc_player.wisdom += 20
        pc_player.fortitude += 10
        pass
    elif pc_race == 'Troll':
        pc_player.strength += 20
        pc_player.agility += 15
        pc_player.intellect += 5
        pc_player.wisdom += 5
        pc_player.fortitude += 25
        pass
    elif pc_race == 'Tauren':
        pc_player.strength += 25
        pc_player.agility += 10
        pc_player.intellect += 5
        pc_player.wisdom += 10
        pc_player.fortitude += 20
        pass
    elif pc_race == 'Orc':
        pc_player.strength += 20
        pc_player.agility += 15
        pc_player.intellect += 10
        pc_player.wisdom += 10
        pc_player.fortitude += 15
        pass


def player_class(pc_player: 'PC', pc_class):
    pc_player.pc_class = pc_class
    if pc_class == 'Warrior':
        pc_player.strength += 20
        pc_player.agility += 20
        pc_player.fortitude += 20
        pass
    elif pc_class == 'Mage':
        pc_player.intellect += 40
        pc_player.wisdom += 20
        pass
    elif pc_class == 'Cleric':
        pc_player.wisdom += 30
        pc_player.intellect += 20
        pc_player.fortitude += 10
        pass


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
