# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:17:52 2023
"""


from threading import Timer, Thread, Event


# as per https://stackoverflow.com/questions/12435211/threading-timer-repeat-function-every-n-seconds
class Scheduler:
    def __init__(self, tim, function):
        self.tim = tim
        self.function = function
        self.thread = Timer(self.tim, self.handle_function)

    def handle_function(self):
        self.function()
        self.thread = Timer(self.tim, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()
