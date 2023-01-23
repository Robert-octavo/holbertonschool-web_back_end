#!/usr/bin/env  python3

"""Returns the first element of the list as a float"""

from typing import List, Union


def safe_first_element(input_list: List[float]) -> Union[float, None]:
    """Returns the first element of the list as a float"""
    if input_list:
        return input_list[0]
    else:
        return None
