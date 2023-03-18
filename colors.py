# -*- coding: utf-8 -*-
"""
@author: Joel Leckie

Created on Sat Mar 11 13:17:52 2023
"""


# Color codes as per colorama online guide
import colorama
colorama.init()


class Effect:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'


class Fore:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    light_grey = '\033[37m'
    dark_grey = '\033[90m'
    light_red = '\033[91m'
    light_green = '\033[92m'
    yellow = '\033[93m'
    light_blue = '\033[94m'
    pink = '\033[95m'
    light_cyan = '\033[96m'


class Back:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    light_grey = '\033[47m'
