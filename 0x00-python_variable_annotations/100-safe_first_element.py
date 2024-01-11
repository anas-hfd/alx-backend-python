#!/usr/bin/env python3
"""any type and unknown """

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ combined elements"""
    if lst:
        return lst[0]
    else:
        return None
    