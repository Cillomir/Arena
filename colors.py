# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:17:52 2023
"""


# Color codes as per colorama online guide
def init():
    import colorama
    colorama.init()


class Effect:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    DISABLE = '\033[02m'
    ITALIC = '\33[03m'
    UNDERLINE = '\033[04m'
    BLINK = '\033[05m'
    BLINK2 = '\033[06m'
    REVERSE = '\033[07m'
    INVISIBLE = '\033[08m'
    STRIKETHROUGH = '\033[09m'


class Fore:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GREY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    PINK = '\033[95m'
    LIGHT_CYAN = '\033[96m'

    def rgb(red, green, blue):
        return f'\u001b[38;2;{red};{green};{blue}m'


class Back:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    ORANGE = '\033[43m'
    BLUE = '\033[44m'
    PURPLE = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'

    def rgb(red, green, blue):
        return f'\u001b[48;2;{red};{green};{blue}m'
