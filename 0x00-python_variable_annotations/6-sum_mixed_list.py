#!/usr/bin/env python3
'''complex: mixed list'''

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''returns the sum of list elements'''
    return float(sum(mxd_list))
