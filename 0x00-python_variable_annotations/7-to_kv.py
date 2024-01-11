#!/usr/bin/env python3
'''str int to tuple'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' returns k & the square of v'''
    return (k, v**2)
