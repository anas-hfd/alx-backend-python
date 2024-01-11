#!/usr/bin/env python3
''''list typed annotation'''

from typing import List, Iterator, Union


def sum_list(input_list: List[float]) -> List[float]:
    '''returns the sum of list elements'''
    return sum(input_list)
