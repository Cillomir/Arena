# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:17:52 2023
"""


from threading import Timer, Lock, Thread, Event


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
