# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:17:52 2023
"""


from threading import Timer, Lock, Thread, Event
import random
import characters
import player
from Items.items import Resource


# as per https://stackoverflow.com/questions/12435211/threading-timer-repeat-function-every-n-seconds
#    and https://stackoverflow.com/questions/2398661/schedule-a-repeating-event-in-python-3
class Scheduler:
    def __init__(self, interval, function):
        self._lock = Lock()
        self._timer = None
        self.interval = interval
        self.function = function
        self.is_running = False
        self.count = 0
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function()
        self.count += 1

    def start(self):
        self._lock.acquire()
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True
        self._lock.release()

    def stop(self):
        self._lock.acquire()
        self._timer.cancel()
        self.is_running = False
        self._lock.release()


def mob_timer_tick():
    for c in characters.Character.all_characters:
        if type(c) is characters.Mob and random.randint(0, 30 - mob_timer.count % 30) <= 5:
            c.move(place.exits(c.loc_x, c.loc_y))
            mob_timer.count = 0
    if len([c for c in characters.Character.all_characters if type(c) is characters.Mob]) < 2:
        if mob_timer.count >= 100 and random.randint(0, 120 - mob_timer.count) < 5:
            rooms = [loc for loc in arena if loc != (player.main_player.loc_x, player.main_player.loc_y)]
            mob_room = rooms[random.choice(rooms)]
            characters.Character.all_characters.append(characters.Fighter(mob_room[0], mob_room[1]))
            mob_timer.count = 0
        else:
            mob_timer.count += 1


def combat_timer_tick(user: player.PC, mob: characters.Mob):
    #combat_timer.count += 1
    user.attack(mob)
    if not mob.dead:
        mob.attack(user)


def resource_ticker_tick():
    #resource_timer.count += 1
    for r in Resource.all_resources:
        if r.node_current < r.node_minimum:
            if r.node_count >= r.node_respawn and random.randint(0, r.node_delay - r.node_count) < 1:
                r.node_current += 1


mob_timer = Scheduler(1, mob_timer_tick)
#combat_timer = schedules.Scheduler(5, combat_timer_tick)
#resource_timer = schedules.Scheduler(10, resource_timer_tick)
