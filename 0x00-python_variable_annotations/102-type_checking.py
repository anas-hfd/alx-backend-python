#!/usr/bin/env python3

'''mypy'''

from typing import Tuple, List, Union, Any


def zoom_array(lst: Union[Tuple[Any, ...], List[Any]],
               factor: int = 2) -> List:
    '''func'''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
