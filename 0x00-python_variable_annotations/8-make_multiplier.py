#!/usr/bin/env python3
'''make multiplier'''

from typing import Callable


def make_multiplier(multiplier: float) -> callable[[float], float]:
    ''' function definition'''
    def float_multiplier(x: float) -> float:
        '''returns the multiplication function'''
        return x * multiplier
    return float_multiplier
