#!/usr/bin/env python3
''' annotation'''

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return'''
    return [(i, len(i)) for i in lst]
